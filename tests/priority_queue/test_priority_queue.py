from ting_file_management.priority_queue import PriorityQueue
import pytest


@pytest.fixture
def mock_regular_priority_2():  # regular_priority_2
    return {
        "nome_do_arquivo": "big_file.txt",
        "qtd_linhas": 100,
        "linhas_do_arquivo": ["big file text"],
    }


@pytest.fixture
def mock_regular_priority_1():  # regular_priority_1
    return {
        "nome_do_arquivo": "medium_file.txt",
        "qtd_linhas": 20,
        "linhas_do_arquivo": ["medium file text"],
    }


@pytest.fixture
def mock_high_priority():  # high_priority -> dequeue e search
    return {
        "nome_do_arquivo": "little_file.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["little file text"],
    }


def test_basic_priority_queueing(
    mock_regular_priority_2, mock_regular_priority_1, mock_high_priority
):
    priority_queue = PriorityQueue()

    priority_queue.enqueue(mock_regular_priority_2)
    assert len(priority_queue) == 1

    priority_queue.enqueue(mock_regular_priority_1)
    assert len(priority_queue) == 2

    priority_queue.enqueue(mock_high_priority)
    assert len(priority_queue) == 3

    file_index_zero = priority_queue.search(0)
    assert file_index_zero == mock_high_priority

    file_index_one = priority_queue.search(1)
    assert file_index_one == mock_regular_priority_2

    file_index_two = priority_queue.search(2)
    assert file_index_two == mock_regular_priority_1

    with pytest.raises(IndexError):
        priority_queue.search(100)

    file_zero_removed = priority_queue.dequeue()
    assert file_zero_removed == mock_high_priority
    assert len(priority_queue) == 2

    file_one_removed = priority_queue.dequeue()
    assert file_one_removed == mock_regular_priority_2
    assert len(priority_queue) == 1

    file_two_removed = priority_queue.dequeue()
    assert file_two_removed == mock_regular_priority_1
    assert len(priority_queue) == 0
