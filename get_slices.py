from nd2reader import ND2Reader
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with ND2Reader('data/20200523_172244_760__Channel561,488_Seq0001-MaxIP.nd2') as images:
        print(len(images))
        print(images.metadata)
        plt.imshow(images[70], cmap='Greys_r')
        print('%d x %d px' % (images.metadata['width'], images.metadata['height']))
        plt.show()
