import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import imageio.v2 as imageio
import os 
import time

def the_current_time():
	print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
	
style = 'style1' 
model = 'samples_%s'% style
content_image = 'content.jpg'
result_image = 'result_%s.jpg'% style
X_image = imageio.imread(content_image)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

saver = tf.train.import_meta_graph(os.path.join(model,'style_transfer_model_final.meta'))
saver.restore(sess,tf.train.latest_checkpoint(model))



graph = tf.get_default_graph()
X = graph.get_tensor_by_name('input:0')
g = graph.get_tensor_by_name('transformer/g:0')

the_current_time()

gen_img = sess.run(g, feed_dict={X:[X_image]})[0]
gen_img = np.clip(gen_img , 0 , 255)/255
imageio.imread(result_image,gen_img)

the_current_time()