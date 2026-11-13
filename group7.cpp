#include <iostream>
#include <vector>
#ifdef _WIN32
#include <windows.h> // кодировка для консоли windows
#endif

std::vector<int> queue;

void printQueue() {
    std::cout << "[";
    for (size_t i = 0; i < queue.size(); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << queue[i];
    }
    std::cout << "]\n";
}

void enqueue(int item) {
    queue.push_back(item);
    std::cout << "enqueue(" << item << "): ";
    printQueue();
}

void dequeue() {
    if (queue.empty()) {
        std::cout << "dequeue: очередь пустая\n";
        return;
    }
    int item = queue.front();
    queue.erase(queue.begin());
    std::cout << "dequeue() == " << item << ": ";
    printQueue();
}

int main() {
#ifdef _WIN32
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
#endif

    enqueue(10);
    enqueue(20);
    enqueue(30);
    dequeue();
    enqueue(40);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    return 0;
}
