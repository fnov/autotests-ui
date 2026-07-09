import re

import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title='', estimated_time='', description='', max_score='0', min_score='0'
        )
        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright', estimated_time='2 weeks', description='Playwright', max_score='100', min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        # Так хотелось написать
        # self.test_create_course(create_course_page, courses_list_page)
        # но, пожалуй, первые 3 пункта задания реализую явно

        index = 0
        title = 'Playwright'
        new_title = 'Python'
        estimated_time = '2 weeks'
        new_estimated_time = '1 month'
        description = 'Playwright'
        new_description = 'Python'
        max_score = '100'
        new_max_score = '10'
        min_score = '10'
        new_min_score = '1'

        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.check_current_url(re.compile(".*#/courses"))
        courses_list_page.course_view.check_visible(
            index=index,
            title=title,
            estimated_time=estimated_time,
            max_score=max_score,
            min_score=min_score
        )

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title=new_title,
            estimated_time=new_estimated_time,
            description=new_description,
            max_score=new_max_score,
            min_score=new_min_score
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.check_current_url(re.compile(".*#/courses"))
        courses_list_page.course_view.check_visible(
            index=index,
            title=new_title,
            estimated_time=new_estimated_time,
            max_score=new_max_score,
            min_score=new_min_score
        )

        # Отдельная проверка description, так как его нет в карточке курса
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.description_textarea.check_have_value(new_description)
        create_course_page.create_course_toolbar.click_create_course_button()
