static Scanner scan = new Scanner(System.in);
static boolean flag = true;
static int B;
static int H;

static {
    B = scan.nextInt();
    H = scan.nextInt();
    try {
        if (B <= 0 || H <= 0) {
            flag = false;
            throw new Exception("Breadth and height must be positive");
        }
    }
    catch(Exception e) {
        System.out.println(e);
    }
}