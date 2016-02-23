// コンパイル
// g++ -o test rpi-stream.cpp `pkg-config --cflags opencv` `pkg-config --libs opencv`


// #include <cv.h>
// #include <highgui.h>
// int main(){
//     cv::VideoCapture cam("http://192.168.100.103:9000/?action=stream"); // カメラ
//     cv::Mat m; // 画像用の変数
//     while((char)cv::waitKey(1)!='q'){
//         cam >> m; // 画像の撮影
//         /* 好きな処理 */
//         cv::imshow("show",m); // 画像の表示
//     }
// }

#include "opencv2/opencv.hpp"

// using namespace cv;

// int main(int, char**)
// {
//     VideoCapture cap("http://192.168.100.103:9000/?action=stream"); // open the default camera
//     if(!cap.isOpened())  // check if we succeeded
//         return -1;

//     Mat edges;
//     namedWindow("edges",1);
//     for(;;)
//     {
//         Mat frame;
//         cap >> frame; // get a new frame from camera
//         cvtColor(frame, edges, CV_BGR2GRAY);
//         GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
//         Canny(edges, edges, 0, 30, 3);
//         imshow("edges", edges);
//         if(waitKey(30) >= 0) break;
//     }
//     // the camera will be deinitialized automatically in VideoCapture destructor
//     return 0;
// }