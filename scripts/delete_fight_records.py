from heroes.models import Fight

def run():
  Fight.objects.all().delete()