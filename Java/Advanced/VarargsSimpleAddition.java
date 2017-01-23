//Write your code here
class Add {
    public void add(int... nums) {
        int sum = nums[0];
        String s = Integer.toString(sum);
        for(int i = 1; i < nums.length; i++) {
            sum += nums[i];
            s += "+" + nums[i];
        }
        System.out.println(String.format("%s=%d", s, sum));
    }
}