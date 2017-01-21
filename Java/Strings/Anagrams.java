    static boolean isAnagram(String a, String b) {
        
        // Complete the function by writing your code here.
        char[] arrA = a.toCharArray();
        char[] arrB = b.toCharArray();
        for(int i = 0; i < arrA.length; i++) {
            arrA[i] = Character.toLowerCase(arrA[i]);
        }
        for(int j = 0; j < arrB.length; j++) {
            arrB[j] = Character.toLowerCase(arrB[j]);
        }
        Arrays.sort(arrA);
        Arrays.sort(arrB);
        return Arrays.equals(arrA, arrB);
    }