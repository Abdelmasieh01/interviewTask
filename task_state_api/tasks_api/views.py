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

        prev = task.state

        if item.is_valid():
            curr = request.POST.get('state', False)
            print(curr)
            if (prev == curr) or (prev == 'dr' and curr == 'ac') or (prev == 'ac' and curr == 'dn') or (curr == 'ar'):
                item.save()
                return Response(data=item.data, status=status.HTTP_202_ACCEPTED)
            else:
               return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        




