#include<iostream>

int main()
{
#ifdef DEBUG
  std::cout << "Hello premake in debug mode" << std::endl;
#endif
#ifdef NDEBUG
  std::cout << "Hello premake in release mode" << std::endl;
#endif
  return 0;
}
