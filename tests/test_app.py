from src.app import create_task, list_tasks

def test_create_task():
    create_task("Teste")
    assert "Teste" in list_tasks()

    