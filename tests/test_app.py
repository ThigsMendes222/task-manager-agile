from src.app import create_task, list_tasks, update_task, complete_task, delete_task, tasks
import pytest

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()

def test_create_task():
    create_task("Teste")
    assert list_tasks()[0]["title"] == "Teste"

def test_update_task():
    create_task("Antigo")
    update_task(0, "Novo")
    assert list_tasks()[0]["title"] == "Novo"

def test_complete_task():
    create_task("Fazer algo")
    complete_task(0)
    assert list_tasks()[0]["done"] == True

def test_delete_task():
    create_task("Apagar")
    delete_task(0)
    assert len(list_tasks()) == 0