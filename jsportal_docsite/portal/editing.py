import os
import codecs
from wtforms import fields, widgets, validators
from flask import request, current_app, flash, redirect
from flask.ext.admin import BaseView, expose, form, expose, helpers
from flask.ext.admin.babel import gettext, lazy_gettext
from flask.ext.admin.contrib import fileadmin

from . import Page

fileExtension = ""

class MarkdownWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs['id'] = 'flask-markdown-' + field.name
        path = request.args.getlist('path')
        fileExtension = path[0].split('.')[1]
        if str(fileExtension) == 'md':
            kwargs['class'] = 'flask-markdown-input col-md-6'
        else:
            kwargs['class'] = 'flask-markdown-input full-width codeMirror'

        html = super(MarkdownWidget, self).__call__(field, **kwargs)
        if str(fileExtension) == 'md':
            return widgets.HTMLString(html + '<div class="preview col-md-6"></div>')            
        else:
            return widgets.HTMLString(html)


class MarkdownField(fields.TextAreaField):
    widget = MarkdownWidget()


class EditForm(form.BaseForm):
    content = MarkdownField(lazy_gettext('Content'), (validators.required(),))


class PortalFileAdmin(fileadmin.FileAdmin):
    editable_extensions = ['md','py', 'html', 'js', 'css', 'txt', 'hrd']

    @expose('/edit/', methods=('GET', 'POST'))
    def edit(self):
        """
            Edit view method
        """

        next_url = None

        path = request.args.getlist('path')

        if not path:
            return redirect(self.get_url('.index'))

        if len(path) > 1:
            next_url = self.get_url('.edit', path=path[1:])

        path = path[0]

        base_path, full_path, path = self._normalize_path(path)

        if not self.is_accessible_path(path) or not self.is_file_editable(path):
            flash(gettext('Permission denied.'))
            return redirect(self._get_dir_url('.index'))

        dir_url = self._get_dir_url('.index', os.path.dirname(path))
        next_url = next_url or dir_url

        form = EditForm(helpers.get_form_data())
        error = False

        if helpers.validate_form_on_submit(form):
            form.process(request.form, content='')
            if form.validate():
                try:
                    with codecs.open(full_path, 'w', encoding='utf-8') as f:
                        f.write(request.form['content'])
                except IOError:
                    flash(gettext("Error saving changes to %(name)s.", name=path), 'error')
                    error = True
                else:
                    self.on_edit_file(full_path, path)
                    flash(gettext("Changes to %(name)s saved successfully.", name=path))
                    return redirect(next_url)
        else:
            try:
                with codecs.open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except IOError:
                flash(gettext("Error reading %(name)s.", name=path), 'error')
                error = True
            except:
                flash(gettext("Unexpected error while reading from %(name)s", name=path), 'error')
                error = True
            else:
                form.content.data = content

        return self.render(self.edit_template, dir_url=dir_url, path=path,
                           form=form, error=error, fileExtension=fileExtension)

