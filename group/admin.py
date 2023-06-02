from django.contrib import admin

from group.models import Teacher, Group, Student

admin.site.register(Teacher)
# admin.site.register(Group)
# admin.site.register(Student)


@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_name', 'groups_list')

    def student_name(self, obj):
        # print(self)
        return obj

    def groups_list(self, obj):
        # print(obj.id, obj.name, obj.last_name, obj.age, obj.contacts)
        # print(obj.groups.all(), '!!!!!!!!!!!!!!')
        return [x for x in obj.groups.all()]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_of_students', 'list_of_students')

    def count_of_students(self, obj):
        print(self)
        # print(obj, '!!!!!!!!!!!!!!!!!!!!!!!')
        qt = obj.students.count()
        # print(qt, '1111111111111111111111')
        return qt

    def list_of_students(self, obj):
        print(self)
        ls = [x for x in obj.students.all()]
        return ls
