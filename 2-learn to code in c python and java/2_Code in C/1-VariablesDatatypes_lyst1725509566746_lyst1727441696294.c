/*
* -----------------------------------------------------------------------------
*
* Copyright <2024> <algorithms365>
*
* Professional Coding Skills Workshops
*
* Licensed under the MIT License:
*
* https://opensource.org/licenses/MIT
*
* For more information about algorithms365:
* Visit Our Skills Website: https://skills.algorithms365.com/
* Our Company Website: https://algorithms365.com/
*
* For Regular Updates Follow & Subscribe Us on Our Social Media Platforms:
* Instagram: https://www.instagram.com/algorithms365/
* YouTube: https://www.youtube.com/@algorithms365
* Facebook: https://www.facebook.com/algorithms365
* Twitter(X): https://x.com/algorithms365
* LinkedIn: https://www.linkedin.com/company/algorithms365-technologies-llp/
*
* Join Our Communities:
* WhatsApp: https://chat.whatsapp.com/K1K7wDMEXG0DJhqMCxFtht
* Telegram: https://t.me/+hyVHXek9WM0zNWQ1
*
* -----------------------------------------------------------------------------
*/
#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

int main() {

     // String
    char name[] = "algorithms365";  // String (character array)
    printf("String: name = %s\n", name);

    // Signed Integer
    int age = 25;  // Integer value
    printf("Integer: age = %d\n", age);

    // Float
    float height = 5.9f;  // Float value
    printf("Float: height = %.2f\n", height);

    // Boolean
    bool is_active = true;  // Boolean value
    printf("Boolean: is_active = %d\n", is_active);

    // Character
    char initial = 'A';  // Character value
    printf("Character: initial = %c\n", initial);

    // Unsigned Character
    unsigned char u_initial = 65;  // Unsigned character value
    printf("Unsigned Character: u_initial = %c\n", u_initial);



    // Unsigned Integer
    unsigned int unsigned_age = 30;  // Unsigned integer value
    printf("Unsigned Integer: unsigned_age = %u\n", unsigned_age);

    // Short Integer
    short int short_age = 20;  // Short integer value
    printf("Short Integer: short_age = %hd\n", short_age);

    // Unsigned Short Integer
    unsigned short int u_short_age = 35;  // Unsigned short integer value
    printf("Unsigned Short Integer: u_short_age = %hu\n", u_short_age);

    // Long Integer
    long int large_number = 1234567890;  // Long integer value
    printf("Long Integer: large_number = %ld\n", large_number);

    // Unsigned Long Integer
    unsigned long int u_large_number = 1234567890UL;  // Unsigned long integer value
    printf("Unsigned Long Integer: u_large_number = %lu\n", u_large_number);

    // 64-bit Integer
    int64_t large_int64 = 9223372036854775807;  // 64-bit integer value
    printf("64-bit Integer: large_int64 = %lld\n", large_int64);

    // Unsigned 64-bit Integer
    uint64_t u_large_int64 = 18446744073709551615U;  // Unsigned 64-bit integer value
    printf("Unsigned 64-bit Integer: u_large_int64 = %llu\n", u_large_int64);



    // Double
    double precise_height = 5.9123456789;  // Double value
    printf("Double: precise_height = %.10f\n", precise_height);

    // Long Double
    long double very_precise_height = 5.9123456789123456789L;  // Long double value
    printf("Long Double: very_precise_height = %.18Lf\n", very_precise_height);

    return 0;
}
