# -*- coding: utf-8 -*-

import _color


class ColorUtils(object):

    @staticmethod
    def GetNameFromColorCode(ColorCode):
        for color_group in _color._COLOR_GROUP:
            if color_group['hex'] == ColorCode:
                return True, color_group['name'], ""
        return False, None, "Color hex not in the list."

    @staticmethod
    def GetHexCodeFromName(name):
        for color_group in _color._COLOR_GROUP:
            if color_group['name'] == name:
                return True, color_group['hex'], ""
        return False, None, "Color name not in the list."


