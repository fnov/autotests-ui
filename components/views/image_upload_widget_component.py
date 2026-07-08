from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Используем компонент EmptyViewComponent
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(
            page, f'{identifier}-image-upload-widget-preview-image', 'Image Upload Preview'
        )

        self.image_upload_info_icon = Icon(
            page, f'{identifier}-image-upload-widget-info-icon', 'Image Upload Icon'
        )
        self.image_upload_info_title = Text(
            page, f'{identifier}-image-upload-widget-info-title-text', 'Image Upload Title'
        )
        self.image_upload_info_description = Text(page,
                                                  f'{identifier}-image-upload-widget-info-description-text',
                                                  'Image Upload Description'
                                                  )

        self.upload_button = Button(
            page, f'{identifier}-image-upload-widget-upload-button', 'Image Upload Button'
        )
        self.remove_button = Button(
            page, f'{identifier}-image-upload-widget-remove-button', 'Image Remove Button'
        )
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Image Upload File')

    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)
