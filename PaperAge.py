#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TTKBootstrap GUI 应用程序
由 TTKBootstrap设计大师 自动生成
生成时间: 2026-01-03 16:51:43

使用说明:
1. 确保已安装 ttkbootstrap: pip install ttkbootstrap
2. 如需支持更多图片格式，请安装 PIL: pip install Pillow
3. 运行此文件: python design.py
"""

import ttkbootstrap as ttk
import tkinter as tk
import os
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.tableview import Tableview

# PIL导入用于支持更多图片格式（JPG, PNG, GIF, BMP等）
try:
    from PIL import Image, ImageTk

    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("警告: PIL未安装，仅支持PNG/GIF格式。安装方法: pip install Pillow")


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='litera')
        self.title('AI DETECTION TOOL FOR PAPER AGE')
        self.geometry('920x670+420+200')
        # 字体配置
        # 创建界面组件
        self.image1_path = r'D:\\Develop\\SouceCode\\PGC-MS-HLB\\App\\\resource\\\PaperAge\\pic1.png'
        self.image1_original = None  # 保存原始PIL图片对象
        self.style.configure('labelframe1.TLabelframe', relief="groove")
        self.labelframe1 = ttk.LabelFrame(self, text="Model setting", bootstyle="default")
        self.combobox1 = ttk.Combobox(self, bootstyle="default", state="readonly", values=["GC-IMS", "IMS"], height=35,
                                      font=("Times New Roman", 10))
        self.label2 = ttk.Label(self, text="Upload Data", bootstyle="default", justify="left", anchor="w")
        self.button1 = ttk.Button(self, text="Click the button", bootstyle="primary", state="normal", takefocus=True,
                                  cursor="hand2")
        self.label3 = ttk.Label(self, text="Select Eigenvalue", bootstyle="default", justify="left", anchor="w")
        self.listbox1 = tk.Listbox(self, state="normal", height=100, fg="#212529", bg="#FFFFFF",
                                   selectbackground="#0D6EFD", selectforeground="#FFFFFF", font=("Times New Roman", 10))
        self.label4 = ttk.Label(self, text="Select Model", bootstyle="default", justify="left", anchor="w")
        self.listbox2 = tk.Listbox(self, state="normal", height=100, fg="#212529", bg="#FFFFFF",
                                   selectbackground="#0D6EFD", selectforeground="#FFFFFF", font=("Times New Roman", 10))
        self.label1 = ttk.Label(self, text="Selection Analysis Method", bootstyle="default", justify="left", anchor="w")
        self.separator1 = ttk.Separator(self, bootstyle="default")
        self.button2 = ttk.Button(self, text="Reset", bootstyle="primary", state="normal", takefocus=True,
                                  cursor="hand2")
        self.button3 = ttk.Button(self, text="Predict", bootstyle="primary", state="normal", takefocus=True,
                                  cursor="hand2")
        self.label6 = ttk.Label(self, text="Model Iterations", bootstyle="default", justify="left", anchor="w")
        self.scale1 = ttk.Scale(self, bootstyle="primary", state="normal", orient="horizontal", from_=0, to=100,
                                value=25, length=200)
        self.style.configure('labelframe2.TLabelframe', relief="groove")
        self.labelframe2 = ttk.LabelFrame(self, text="Application Description", bootstyle="default")
        self.style.configure('labelframe4.TLabelframe', relief="groove")
        self.labelframe4 = ttk.LabelFrame(self, text="Prediction", bootstyle="default")
        self.style.configure('labelframe3.TLabelframe', relief="groove")
        self.labelframe3 = ttk.LabelFrame(self, text="Interpretation Of Prediction Conclusion", bootstyle="default")
        self.label8 = ttk.Label(self, text="Note:", bootstyle="default", justify="left", anchor="w",
                                font=("Times New Roman", 20))
        self.text1 = ttk.Text(self, font=("Times New Roman", 11), height=4, width=81, borderwidth=0.0, padx=1.0,
                              relief="flat",  # 普通边框样式
                              highlightthickness=0,  # 高亮边框宽度（必须>0才能显示）
                              highlightcolor="white",  # 焦点时高亮颜色
                              highlightbackground="white")
        self.text2 = ttk.Text(self, font=("Times New Roman", 11), height=3, width=81, borderwidth=0.0, relief="flat",
                              highlightthickness=0,  # 高亮边框宽度（必须>0才能显示）
                              highlightcolor="white",  # 焦点时高亮颜色
                              highlightbackground="white")
        self.label9 = ttk.Label(self, text="Model Interpretation", bootstyle="default", justify="left", anchor="w",
                                font=("Times New Roman", 20))
        self.image1 = ttk.Label(self)
        self.image2 = ttk.Label(self)
        self.label10 = ttk.Label(self, text="Prediction Results", bootstyle="default", justify="left", anchor="w",
                                 font=("Times New Roman", 20))
        self.label11 = ttk.Label(self, text="The time before the detected paper is:", bootstyle="default",
                                 justify="left", anchor="w", font=("Times New Roman", 12))
        self.label12 = ttk.Label(self, text="8.93 Years", bootstyle="default", justify="left", anchor="w",
                                 font=("Times New Roman", 20), foreground="#006400")
        self.floodgauge1 = ttk.Floodgauge(self, bootstyle="primary", font=("Times New Roman", 12), mode="determinate",
                                          maximum=17, value=9, text="Paper Age", length=300, orient="horizontal")

        # 布局管理
        # Place 布局组件
        self.labelframe1.place(x=10, y=5, width=220, height=655)
        self.combobox1.place(x=20, y=70, width=180, height=35)
        # 设置当前选中索引
        if self.combobox1['values']:  # 确保有选项
            try:
                idx = min(0, len(self.combobox1['values']) - 1)  # 防止索引越界
                self.combobox1.current(idx)
            except (tk.TclError, IndexError) as e:
                print(f"警告: 设置 combobox1 索引失败 - {e}")
        self.label2.place(x=20, y=120, width=155, height=30)
        self.button1.place(x=20, y=150, width=180, height=40)
        self.label3.place(x=20, y=200, width=155, height=30)
        self.listbox1.place(x=20, y=230, width=180, height=100)
        # 配置Listbox颜色和样式（覆盖主题默认值）
        self.listbox1.configure(fg="#212529")
        self.listbox1.configure(bg="#ffffff")
        self.listbox1.configure(selectbackground="#0d6efd")
        self.listbox1.configure(selectforeground="#ffffff")
        self.listbox1.configure(relief="sunken")
        self.listbox1.configure(borderwidth=1)
        # 添加列表项
        self.listbox1.insert("end", "Neryl acetate")
        self.listbox1.insert("end", "Isomenthone")
        self.listbox1.insert("end", "Nonanal-D")
        self.listbox1.insert("end", "Cyclohexanone")
        self.listbox1.insert("end", "Heptanal-M")
        self.listbox1.insert("end", "Amyl alcohol")
        self.listbox1.insert("end", "1-Butanol-D")
        self.listbox1.insert("end", "Pyrazine")
        self.listbox1.selection_set(0)
        self.listbox1.activate(0)
        # 添加滚动条
        self.listbox1_scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.listbox1_scrollbar.place(x=200, y=230, width=20, height=100)
        self.listbox1.configure(yscrollcommand=self.listbox1_scrollbar.set)
        self.listbox1_scrollbar.configure(command=self.listbox1.yview)
        self.label4.place(x=20, y=340, width=155, height=30)
        self.listbox2.place(x=20, y=370, width=180, height=100)
        # 配置Listbox颜色和样式（覆盖主题默认值）
        self.listbox2.configure(fg="#212529")
        self.listbox2.configure(bg="#ffffff")
        self.listbox2.configure(selectbackground="#0d6efd")
        self.listbox2.configure(selectforeground="#ffffff")
        self.listbox2.configure(relief="sunken")
        self.listbox2.configure(borderwidth=1)
        # 添加列表项
        self.listbox2.insert("end", "CatBoost")
        self.listbox2.insert("end", "RandomForest")
        self.listbox2.insert("end", "DecisionTree")
        self.listbox2.insert("end", "XGBoost")
        self.listbox2.insert("end", "AdaBoost")
        self.listbox2.selection_set(0)
        self.listbox2.activate(0)
        # 添加滚动条
        self.listbox2_scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.listbox2_scrollbar.place(x=200, y=370, width=20, height=100)
        self.listbox2.configure(yscrollcommand=self.listbox2_scrollbar.set)
        self.listbox2_scrollbar.configure(command=self.listbox2.yview)
        self.label1.place(x=20, y=40, width=155, height=30)
        self.separator1.place(x=20, y=570, width=200, height=5)
        self.button2.place(x=15, y=600, width=100, height=30)
        self.button3.place(x=125, y=600, width=100, height=30)
        self.label6.place(x=20, y=485, width=155, height=30)
        self.scale1.place(x=20, y=520, width=200, height=35)
        self.labelframe2.place(x=235, y=5, width=675, height=195)
        self.labelframe4.place(x=235, y=440, width=675, height=220)
        self.labelframe3.place(x=235, y=200, width=675, height=240)
        self.label8.place(x=250, y=20, width=68, height=40)
        self.text1.place(x=250, y=60, width=645, height=65)
        self.text1.insert("1.0",
                          "A.Machine learning (e.g., Random Forest, XGBoost) leverages GC-IMS features to "
                          "learn age-related patterns. It automates analysis, handles high-dimensional data, "
                          "and enables rapid, accurate non-destructive dating, supporting artifact "
                          "authentication and preservation.")
        self.text1.configure(borderwidth=0.0)
        self.text2.place(x=250, y=125, width=645, height=65)
        self.text2.insert("1.0",
                          "B.Paper dating is crucial for cultural heritage, forensics, "
                          "and archives. Traditional subjective or destructive methods have limitations, "
                          "while GC-IMS provides non-destructive chemical fingerprints (VOC profiles) that evolve "
                          "with paper aging, enabling objective chronological classification without "
                          "damaging specimens.")
        self.text2.configure(borderwidth=0.0)
        self.label9.place(x=250, y=240, width=240, height=30)
        self.image1.place(x=250, y=280, width=450, height=120)
        # 加载原始图片 (image1 - 自适应模式)
        if PIL_AVAILABLE and os.path.exists(self.image1_path):
            try:
                self.image1_original = Image.open(self.image1_path)
                # 延迟初始加载，确保窗口已渲染
                self.after(100, self._resize_image1)
                # 绑定窗口大小变化事件
                self.image1.bind("<Configure>", lambda e: self._resize_image1())
            except Exception as e:
                print(f"加载图片失败 (image1): {e}")
                self.image1.configure(text="图片加载错误")
        else:
            self.image1.configure(text="图片文件不存在或PIL未安装")

        self.image2.place(x=710, y=230, width=190, height=190)
        try:
            image_path_image2 = r'D:\\Develop\\SouceCode\\PGC-MS-HLB\\App\\\resource\\\PaperAge\\pic2.png'
            if os.path.exists(image_path_image2):
                if PIL_AVAILABLE:
                    # 使用PIL加载图片（支持更多格式，适配方式: fill）
                    pil_image_image2 = Image.open(image_path_image2)
                    # 获取Label的宽高
                    self.update_idletasks()
                    label_width = self.image2.winfo_width()
                    label_height = self.image2.winfo_height()
                    if label_width > 1 and label_height > 1:
                        # 根据适配方式处理图片
                        original_width, original_height = pil_image_image2.size
                        fit_mode = "fill"
                        if fit_mode == "fill":
                            # 填充整个容器，可能会拉伸图片
                            pil_image_image2 = pil_image_image2.resize((label_width, label_height),
                                                                       Image.Resampling.LANCZOS)
                        elif fit_mode == "contain":
                            # 保持纵横比，完整显示图片
                            scale = min(label_width / original_width, label_height / original_height)
                            new_width = int(original_width * scale)
                            new_height = int(original_height * scale)
                            pil_image_image2 = pil_image_image2.resize((new_width, new_height),
                                                                       Image.Resampling.LANCZOS)
                        elif fit_mode == "cover":
                            # 保持纵横比，填充整个容器，可能会裁剪图片
                            scale = max(label_width / original_width, label_height / original_height)
                            new_width = int(original_width * scale)
                            new_height = int(original_height * scale)
                            temp_image = pil_image_image2.resize((new_width, new_height), Image.Resampling.LANCZOS)
                            # 裁剪到目标尺寸
                            left = (new_width - label_width) // 2
                            top = (new_height - label_height) // 2
                            right = left + label_width
                            bottom = top + label_height
                            pil_image_image2 = temp_image.crop((left, top, right, bottom))
                        elif fit_mode == "fitWidth":
                            # 适应宽度，保持纵横比
                            scale = label_width / original_width
                            new_height = int(original_height * scale)
                            pil_image_image2 = pil_image_image2.resize((label_width, new_height),
                                                                       Image.Resampling.LANCZOS)
                            if new_height > label_height:
                                # 如果高度超出，居中裁剪
                                top = (new_height - label_height) // 2
                                pil_image_image2 = pil_image_image2.crop((0, top, label_width, top + label_height))
                        elif fit_mode == "fitHeight":
                            # 适应高度，保持纵横比
                            scale = label_height / original_height
                            new_width = int(original_width * scale)
                            pil_image_image2 = pil_image_image2.resize((new_width, label_height),
                                                                       Image.Resampling.LANCZOS)
                            if new_width > label_width:
                                # 如果宽度超出，居中裁剪
                                left = (new_width - label_width) // 2
                                pil_image_image2 = pil_image_image2.crop((left, 0, left + label_width, label_height))
                        else:  # fit_mode == "none" 不缩放，使用原图
                            # 原始大小，如果超出目标尺寸则居中裁剪，否则居中放置
                            if original_width > label_width or original_height > label_height:
                                # 需要裁剪
                                left = max(0, (original_width - label_width) // 2)
                                top = max(0, (original_height - label_height) // 2)
                                right = min(original_width, left + label_width)
                                bottom = min(original_height, top + label_height)
                                pil_image_image2 = pil_image_image2.crop((left, top, right, bottom))
                            elif original_width < label_width or original_height < label_height:
                                # 需要居中放置在透明背景上
                                final_image = Image.new("RGBA", (label_width, label_height), (0, 0, 0, 0))
                                offset_x = (label_width - original_width) // 2
                                offset_y = (label_height - original_height) // 2
                                final_image.paste(pil_image_image2, (offset_x, offset_y))
                                pil_image_image2 = final_image
                    self.image2_photo = ImageTk.PhotoImage(pil_image_image2)
                elif image_path_image2.lower().endswith((".png", ".gif")):
                    # 使用tkinter.PhotoImage（仅支持PNG/GIF）
                    self.image2_photo = tk.PhotoImage(file=image_path_image2)
                else:
                    print(f"图片格式不支持，需要安装PIL: {image_path_image2}")
                    self.image2_photo = None

                if hasattr(self, "image2_photo") and self.image2_photo:
                    self.image2.configure(image=self.image2_photo, text="")
                else:
                    self.image2.configure(text="图片加载失败")
            else:
                print(f"图片文件不存在: {image_path_image2}")
                self.image2.configure(text="图片文件不存在")
        except Exception as e:
            print(f"加载图片失败 (image2): {e}")
            self.image2.configure(text="图片加载错误")

        self.label10.place(x=250, y=465, width=320, height=30)
        self.label11.place(x=250, y=510, width=423, height=30)
        self.label12.place(x=250, y=545, width=240, height=30)
        self.floodgauge1.place(x=250, y=600, width=620, height=35)

    def _resize_image1(self):
        """调整图片大小以适应Label (image1) - 适配方式: fill"""
        # 防止递归调用
        if hasattr(self, "_image1_resizing") and self._image1_resizing:
            return
        if not self.image1_original:
            return

        try:
            self._image1_resizing = True

            # 获取Label当前大小
            target_width = self.image1.winfo_width()
            target_height = self.image1.winfo_height()

            if target_width > 1 and target_height > 1:
                # 获取原始图片尺寸
                original_width, original_height = self.image1_original.size

                # 根据适配方式处理图片
                fit_mode = "fill"
                if fit_mode == "fill":
                    # 填充整个容器，可能会拉伸图片
                    resized_image = self.image1_original.resize((target_width, target_height), Image.Resampling.LANCZOS)
                elif fit_mode == "contain":
                    # 保持纵横比，完整显示图片
                    scale = min(target_width / original_width, target_height / original_height)
                    new_width = int(original_width * scale)
                    new_height = int(original_height * scale)
                    resized_image = self.image1_original.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    # 创建目标尺寸的透明背景
                    final_image = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
                    offset_x = (target_width - new_width) // 2
                    offset_y = (target_height - new_height) // 2
                    final_image.paste(resized_image, (offset_x, offset_y))
                    resized_image = final_image
                elif fit_mode == "cover":
                    # 保持纵横比，填充整个容器，可能会裁剪图片
                    scale = max(target_width / original_width, target_height / original_height)
                    new_width = int(original_width * scale)
                    new_height = int(original_height * scale)
                    temp_image = self.image1_original.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    # 裁剪到目标尺寸
                    left = (new_width - target_width) // 2
                    top = (new_height - target_height) // 2
                    right = left + target_width
                    bottom = top + target_height
                    resized_image = temp_image.crop((left, top, right, bottom))
                elif fit_mode == "fitWidth":
                    # 适应宽度，保持纵横比
                    scale = target_width / original_width
                    new_height = int(original_height * scale)
                    resized_image = self.image1_original.resize((target_width, new_height), Image.Resampling.LANCZOS)
                    if new_height > target_height:
                        # 如果高度超出，居中裁剪
                        top = (new_height - target_height) // 2
                        resized_image = resized_image.crop((0, top, target_width, top + target_height))
                    elif new_height < target_height:
                        # 如果高度不足，居中放置在透明背景上
                        final_image = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
                        offset_y = (target_height - new_height) // 2
                        final_image.paste(resized_image, (0, offset_y))
                        resized_image = final_image
                elif fit_mode == "fitHeight":
                    # 适应高度，保持纵横比
                    scale = target_height / original_height
                    new_width = int(original_width * scale)
                    resized_image = self.image1_original.resize((new_width, target_height), Image.Resampling.LANCZOS)
                    if new_width > target_width:
                        # 如果宽度超出，居中裁剪
                        left = (new_width - target_width) // 2
                        resized_image = resized_image.crop((left, 0, left + target_width, target_height))
                    elif new_width < target_width:
                        # 如果宽度不足，居中放置在透明背景上
                        final_image = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
                        offset_x = (target_width - new_width) // 2
                        final_image.paste(resized_image, (offset_x, 0))
                        resized_image = final_image
                else:  # none 或其他值
                    # 不缩放，原始大小，如果超出目标尺寸则居中裁剪，否则居中放置
                    if original_width > target_width or original_height > target_height:
                        # 需要裁剪
                        left = max(0, (original_width - target_width) // 2)
                        top = max(0, (original_height - target_height) // 2)
                        right = min(original_width, left + target_width)
                        bottom = min(original_height, top + target_height)
                        resized_image = self.image1_original.crop((left, top, right, bottom))
                    elif original_width < target_width or original_height < target_height:
                        # 需要居中放置在透明背景上
                        final_image = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
                        offset_x = (target_width - original_width) // 2
                        offset_y = (target_height - original_height) // 2
                        final_image.paste(self.image1_original, (offset_x, offset_y))
                        resized_image = final_image
                    else:
                        # 尺寸完全匹配
                        resized_image = self.image1_original

                # 转换为PhotoImage
                self.image1_photo = ImageTk.PhotoImage(resized_image)
                # 更新Label
                self.image1.configure(image=self.image1_photo, text="")
        except Exception as e:
            print(f"Image resize error (image1): {e}")
        finally:
            self._image1_resizing = False


if __name__ == '__main__':
    app = App()
    app.mainloop()
