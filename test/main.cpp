#include "http_parser.h"
#include <iostream>

int main () {
    http_parser parser;
    http_parser_init(&parser, HTTP_REQUEST);
	std::cout << "OK\n";
	return 0;
}
