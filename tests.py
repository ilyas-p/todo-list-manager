from todo_manager import TodoManager


def test_add_task():
    manager = TodoManager()

    result = manager.add_task("Learn Python")

    assert result is True
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Learn Python"

    print("✓ test_add_task passed")


def test_complete_task():
    manager = TodoManager()

    manager.add_task("Learn Python")

    result = manager.complete_task(1)

    assert result is True
    assert manager.tasks[0].completed is True

    print("✓ test_complete_task passed")


def test_remove_task():
    manager = TodoManager()

    manager.add_task("Learn Python")
    manager.add_task("Study Git")

    result = manager.remove_task(1)

    assert result is True
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Study Git"

    print("✓ test_remove_task passed")


def test_empty_task():
    manager = TodoManager()

    result = manager.add_task("")

    assert result is False
    assert len(manager.tasks) == 0

    print("✓ test_empty_task passed")


def test_invalid_task_number():
    manager = TodoManager()

    manager.add_task("Learn Python")

    result = manager.remove_task(99)

    assert result is False
    assert len(manager.tasks) == 1

    print("✓ test_invalid_task_number passed")


if __name__ == "__main__":
    test_add_task()
    test_complete_task()
    test_remove_task()
    test_empty_task()
    test_invalid_task_number()

    print("\nAll tests passed successfully!")