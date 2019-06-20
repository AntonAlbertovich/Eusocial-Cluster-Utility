#include <stdio.h>
int main() {
int month, year;
printf("Enter the month as a number:");
scanf("%d",&month);
printf("Enter the year:");
scanf("%d", &year);

if (month <= 7){
     if (month % 2 == 0){
          if (month == 2){
               if(year % 4 == 0){
                    printf("29 days are in this month \n");
                }
               else
                {
                     printf("28 days are in this month \n");
                }
            }
          else
            {
               printf("30 days are in this month \n");
            }
        }
     else
        {
          printf("31 days are in this month \n");
        }
}
else if(month % 2 == 0){
     printf("31 days are in this month \n");
}
else
{
     printf("30 days are in this month \n");
}
return 0;
}




