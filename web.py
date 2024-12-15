from flask import Flask, render_template, request, send_from_directory, url_for
import os

app = Flask(__name__)

# 配置路径
UPLOAD_FOLDER = "uploads"
RENAMED_FOLDER = "renamed"
LOCAL_IMAGES_FOLDER = "static/images"
GENERATED_FOLDER = "generated"  # 用于存放生成的图片
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RENAMED_FOLDER"] = RENAMED_FOLDER
app.config["GENERATED_FOLDER"] = GENERATED_FOLDER

# 确保文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RENAMED_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    renamed_image = None
    selected_image = None
    generated_image = None

    if request.method == "POST":
        action = request.form.get("action")

        if action == "upload":
            # 上传风格图片
            file = request.files.get("file")
            if file:
                new_filename = "style.jpg"
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
                file.save(file_path)          
                os.system("python basetrans.py")                 
                uploaded_image = "change.jpg"

        elif action == "rename_upload":
            # 上传并改名
            file = request.files.get("rename_file")
            if file:
                new_filename = "change.jpg"
                renamed_path = os.path.join(app.config["RENAMED_FOLDER"], new_filename)
                file.save(renamed_path) 
                renamed_image = new_filename

        elif action == "select":
            # 展示选定风格迁移后图片
            selected_image = request.form.get("local_image")

            # 调用生成图片脚本
            if selected_image:
                style_number = selected_image.split(".")[0][-1]  # 提取风格编号
                generated_filename = f"{style_number}.jpg"
                generated_path = os.path.join(app.config["GENERATED_FOLDER"], generated_filename)

                # 运行生成脚本并保存图片
                # command = f"python3 generate_pic.py {style_number} {generated_path}"
                # os.system(command)  # 运行命令
                if int(style_number)==1:
                    print(111)
                    os.system("python usingmodel1.py")  
                elif int(style_number)==2:
                    print(222)
                    os.system("python usingmodel2.py")  
                elif int(style_number)==3:
                    print(333)
                    os.system("python usingmodel3.py")  
                generated_image = generated_filename
                # print(f"Executed command: {command}")

        elif action == "clear":
            # 清空图片
            uploaded_image = None
            renamed_image = None
            selected_image = None
            generated_image = None

    return render_template(
        "index.html",
        uploaded_image=uploaded_image,
        renamed_image=renamed_image,
        selected_image=selected_image,
        generated_image=generated_image,
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/renamed/<filename>")
def renamed_file(filename):
    return send_from_directory(app.config["RENAMED_FOLDER"], filename)


@app.route("/generated/<filename>")
def generated_file(filename):
    return send_from_directory(app.config["GENERATED_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
