// class HelloWorld 
// {

//     // static void typecast() {
//     //     double d1 = 5.5;
//     //     short d2 = 10;

//     //     int z = (int) d1;
//     //     double x = (double) d2;

//     //     System.out.printf("Typecast 1 = %d\n",z);
//     //     System.out.printf("Typecast 2 = %d",x);
//     // }

//     public static void main(String[] args) {

    

//         // int a = 2;
//         // int b = 5;
//         // int max = (a > b) ? a : b;

//         // System.out.printf("Maximum value=%d\n",max);
//         // typecast();
//     }
// }

// //java keywords
// // abstract, boolean, break, continue
// // byte,case,catch,char,class,continue,default,do,double,else,enum,extends,final,finally,for,if,implements,import,instanceof,int,interface,int,long,native,new,null
// // public return short static strictfp super switch synchronized this throw throws transient try void volatile while

public class HelloWorld {
    static int a = 10;

    private void method1() {
        int a = 20;
        System.out.println("a inside method1 %d"+ a);
        this.a = 30;
        System.out.println("a inside method1 after %d"+a);
    }

    private void method2() {
        System.out.println("Value of a in method2 %d"+ a);
    }

    public static void main(String args[]) {
        System.out.println("Inside main "+ a);
        HelloWorld h = new HelloWorld();
        h.method1();
        h.method2();
    }
}
