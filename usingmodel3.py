import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import scipy.io
import scipy.misc
import os
import time
from PIL import Image
import imageio.v2 as imageio

#这个是跑gpu
with tf.device("/gpu:0"):
    a = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[2,3])
    b = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],shape=[3,2])
    c = tf.matmul(a,b)
    #查看计算时硬件的使用情况
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    print(sess.run(c))
  
#打印时间函数
def the_current_time():
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))

#style 填风格图的名称就行
style = 'style5' 
model = os.path.join('samples_styles', style)
#model = 'samples_styles%s'% style 
#content_image = 'content.jpg'
CONTENT_IMG = os.path.join('renamed', 'change.jpg')
result_image = os.path.join('generated', '3.jpg')
#result_image = 'result_%s.jpg'% style
X_image = imageio.imread(CONTENT_IMG)


config = tf.ConfigProto()
config.gpu_options.allow_growth = True

# with tf.Session(config=config) as sess:
sess=tf.Session()
sess.run(tf.global_variables_initializer())

saver = tf.train.import_meta_graph(os.path.join(model,'fast_style_transfer.meta'))
saver.restore(sess,tf.train.latest_checkpoint(model))




#现在问题找不到input，怀疑是没存进去？
graph = tf.get_default_graph()
X = graph.get_tensor_by_name('X:0')
g = graph.get_tensor_by_name('transformer/g:0')

the_current_time()

gen_img = sess.run(g, feed_dict={X:[X_image]})[0]
gen_img = np.clip(gen_img, 0, 255).astype(np.uint8)
imageio.imwrite(result_image, gen_img)

the_current_time()