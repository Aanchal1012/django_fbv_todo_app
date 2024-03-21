from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

def due_time():
    """
    globally declared time for task to be completed
    :return:
    """
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    """
    :param
    class for ToDoList model, it is extending the models.Model superclass
    """
    list_title = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        """
        a django convention method to return the URL for particular data item, allows to reference the URL easily
        reverse is used to avoid hard-coding the URL and its param
        id is the default and unique generated identififer for each object in django
        :return:
        """
        return reverse("list", args=[self.id])

    def __str__(self):
        """
        to create a readable representation of the object
        :return:
        """
        return self.list_title


class ToDoTasks(models.Model):
    """
    class :
    """
    objects = None
    task_title = models.CharField(max_length=255)  # task name
    description = models.TextField(null=True, blank=True)  # task description , can be empty
    create_date = models.DateTimeField(auto_now_add=True)  # task create date, set to automatically pick up
    due_date = models.DateTimeField(default=due_time)  # task end date, set to be per due_time global func
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # todo_list links ToDoTasks back to ToDoList and ensures that each task belongs to exactly one list
    # on_delete ensures that if a list is deleted then all its associate to-do task also gets deleted

    def get_absolute_url(self):
        """
        a django convention method to return the URL for particular data item, allows to reference the URL easily
        reverse is used to avoid hard-coding the URL and its param
        :return:
        """
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        """
        to create a readable representation of each object
        :return:
        """
        return f"{self.task_title}: due{self.due_date}"

    class Meta:
        """
            class : nested MetaData class that allows us to set some useful options like ordering the ToDoTask records
            """
        ordering = ["due_date"]
