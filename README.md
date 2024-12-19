# image_style_transfer
## 项目简介
一个图像风格迁移的项目
## 项目使用说明
1. 需要有一个预训练vgg19模型(imagenet-vgg-verydeep-19.mat)
2. basetrans.py为基础图像风格迁移的代码，同目录下的content.jpg作为内容图，同目录下的style1.jpg作为风格图
3. quick.py为生成快速图像风格迁移模型的代码,可根据自己的喜好进行训练
4. quick.py训练时需要基础图库作为内容图,放在同目录下的train文件夹中，风格图片放在同目录下的styles文件中，通过修改代码中的参数style_index来指定文件夹styles中对应的风格图片
5. 使用quick代码训练后得到的模型会被放在sample_style下，使用usingmodel.py函数来使用这个模型
6. 该项目有一个web脚本可以使用,运行web.py即可运行usingmodel.py代码来使用快速图像风格迁移的模型来进行实时的图像风格迁移，结果将会被展示在网页上
