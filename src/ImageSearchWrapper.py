from python_imagesearch.imagesearch import imagesearch


class ImageSearchWrapper:

    def chat(self):
        pos = imagesearch('C:/Users/Leonard/PycharmProjects/amongus/images/chat2.png')
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print('image not found')
        return pos

    def garbage(self):
        pos = imagesearch('C:/Users/Leonard/PycharmProjects/amongus/images/garbage_handle.png')
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print('image not found')
        return pos

    def divert_power(self):
        pos = imagesearch('C:/Users/Leonard/PycharmProjects/amongus/images/divert_power.png')
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print('image not found')
        return pos

    def divert_power2(self):
        pos = imagesearch('C:/Users/Leonard/PycharmProjects/amongus/images/divert_power2.png')
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print('image not found')
        return pos

    def wires(self):
        pos = imagesearch('C:/Users/Leonard/PycharmProjects/amongus/images/blue_wire.png')
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
        else:
            print('image not found')
        return pos