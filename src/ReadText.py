from PIL import Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Leonard\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


class ReadText:

    def ocr_core(self, filename):
        """
        This function will handle the core OCR processing of images.
        """
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
        text = pytesseract.image_to_string(threshold, lang='eng')
        return text

    def read_tasks(self, filename):
        # Finds tasks list and reads output
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # High threshold because new tasks will be white
        ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(threshold, lang='eng')
        return text


if __name__ == '__main__':
    readtext = ReadText()
    print(readtext.ocr_core('C:/Users/Leonard/PycharmProjects/amongus/images/Test_tasks.png'))
    # print(ocr_core('C:\\Users\\Leonard\\PycharmProjects\\amongus\\images\\Test_tasks2.png'))
