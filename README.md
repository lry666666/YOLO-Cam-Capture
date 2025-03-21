# YOLO-Cam-Capture

# 摄像头拍照上传项目

这是一个使用 HTML、JavaScript 和 Python (Flask) 构建的简单 Web 应用程序，允许用户使用电脑摄像头拍照，并将照片上传到本地服务器。

## 项目概述

此项目包含以下主要功能：

*   **摄像头访问：** 使用户能够通过浏览器访问其电脑摄像头。
*   **拍照：**  点击按钮即可拍摄当前摄像头画面照片。
*   **上传：**  将拍摄的照片自动上传到服务器。
*   **服务端存储：** 使用 Python (Flask) 后端接收并保存上传的照片。
*   **状态显示:** 前端界面会显示上传状态 (成功/失败/上传中)。

## 技术栈

*   **前端：**
    *   HTML
    *   CSS (用于样式美化)
    *   JavaScript
*   **后端：**
    *   Python
    *   Flask (Web 框架)
    *   Pillow (图像处理库)
    *   flask-cors (处理跨域资源共享)

