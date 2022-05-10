from .models import Task
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API for basic CRUD operations.
    """
    queryset = Task.objects.all().order_by('-timestamp')
    serializer_class = TaskSerializer

    """
    I edited the update endpoint to prevent the user from going backwards
    on the task workflow.
    """
    def update(self, request, pk=None):
        task = Task.objects.get(pk=pk)
        item = TaskSerializer(instance=task, data=request.data)

        #Previous state before update
        prev = task.state

        if item.is_valid():
            #Current state from the form
            curr = int(request.POST.get('state', False))
            if (prev == curr) or (curr - prev == 1) or (curr == 3):
                item.save()
                return Response(data=item.data, status=status.HTTP_202_ACCEPTED)
            else:
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        




