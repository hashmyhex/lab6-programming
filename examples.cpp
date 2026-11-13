#include <array>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>
#ifdef _WIN32
#include <windows.h> // кодировка для консоли windows
#endif

int main() {
#ifdef _WIN32
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
#endif

    // обычный массив
    int arr[5] = {5, 4, 3, 2, 1};
    std::cout << "arr: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n";

    // std::array
    std::array<int, 5> fixed = {1, 2, 3, 4, 5};
    std::cout << "std::array, размер == " << fixed.size() << ", первый == " << fixed.front() << "\n";

    // std::vector
    std::vector<int> numbers = {3, 1, 4, 1, 5};
    numbers.push_back(9);
    numbers.insert(numbers.begin() + 1, 7);
    numbers.erase(numbers.begin());
    std::cout << "vector: ";
    for (int x : numbers) std::cout << x << " ";
    std::cout << "\nразмер == " << numbers.size() << "\n";

    // std::tuple
    std::tuple<std::string, int, double> student = {"Иван", 25, 4.5};
    std::cout << "tuple: " << std::get<0>(student) << ", " << std::get<1>(student) << ", "
              << std::get<2>(student) << "\n";

    return 0;
}
