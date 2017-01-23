class Printer
{
   public <E> void printArray(E[] arr) {
       for(int i = 0; i < arr.length; i++) {
           System.out.println(arr[i]);
       }
   }
}