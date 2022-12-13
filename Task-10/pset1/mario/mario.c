#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int row = 0; row < height; row++)
    {
        for (int space = height - row - 1; space > 0; space--)
        {
            printf(" ");
        }
        for (int h = 0; h < row + 1; h++)
        {
            printf("#");
        }
        printf("\n");
    }
}
