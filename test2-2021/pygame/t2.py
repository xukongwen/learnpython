# coding=utf-8


import os

import pygame


def blit_text(surface, text, pos, font, color=pygame.Color(255, 255, 255)):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x = pos[0] + 10
    y = pos[1]
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] + 10
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0] + 10
        y += word_height + 2


class EarthGodDialog:
    def __init__(self, head_img, text , multiple, is_expand):
        """
        对话框的实现类
        :param head_img:人物的头像路径
        :param text: 对话框中的文字
        """
        temp_header = head_img
        if is_expand:
            head_w = int(temp_header.get_width() ** multiple)
            head_h = int(temp_header.get_height() ** multiple)
        else:
            head_w = int(temp_header.get_width() // multiple)
            head_h = int(temp_header.get_height() // multiple)
        # 头像大小改变
        head = pygame.transform.scale(temp_header, (head_w, head_h))
        # 对话框图片
        dialog_path = os.path.join('./img/box1.png')
        temp_dialog = pygame.image.load(dialog_path)
        dialog_w = temp_dialog.get_width() // 3
        dialog_h = temp_dialog.get_height() // 3
        # 对话框缩小一半
        dialog = pygame.transform.scale(temp_dialog, (dialog_w, dialog_h))
        # 绘制汉字
        # font_path = os.path.join('./resource/font/迷你简粗宋.TTF')
        font = pygame.font.Font("KKong3", 18)

        blit_text(dialog, text, (10, 10), font)

        # 生成surface并绘制
        if head_h > dialog_h:
            h = head_h
        else:
            h = dialog_h
        w = head_w + dialog_w
        self.surface = pygame.Surface((w, h))
        # 设置关键色，形成透明图片
        self.surface.set_colorkey((0, 0, 0))
        # 绘制
        self.surface.blit(head, (0, 0))
        self.surface.blit(dialog, (head_w, 0))