from PIL import Image

# Write a script that compares an untrusted image of Rao to a trusted image of
# our Grand Leader. If the image has been modified from the original, it is NOT
# Rao Compliant. Rao is Grand!


def compare_images(trusted, untrusted):

    if trusted.size != untrusted.size:
        return False

    width, height = trusted.size
    for posy in xrange(width):
        for posx in xrange(height):
            if trusted.getpixel((posy, posx)) != untrusted.getpixel((posy, posx)):
                return False

    return True


def main():

    with open('trusted.png', 'rb') as fd_trusted, open('untrusted01.png', 'rb') as fd_untrusted:
        trusted_img = Image.open(fd_trusted)
        untrusted_img = Image.open(fd_untrusted)

        same = compare_images(trusted_img, untrusted_img)

        if same:
            print 'Image is Rao Compliant!'
        else:
            print 'Image is NOT Rao Compliant!'


if __name__ == '__main__':
    main()
