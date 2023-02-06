from src.myimage import MyImage


def remove_channel(src: MyImage, red: bool = False, green: bool = False,
                   blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.

    Suppresses the red channel if no channel is indicated. src is not modified.

    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.

    Returns:
    a copy of src with the indicated channels suppressed.
    """
    pass


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image whose rotations have to be stored and returned.

    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    pass


def apply_mask(src: MyImage, maskfile: str, average: bool = True) -> MyImage:
    """Returns an copy of src with the mask from maskfile applied to it.

    maskfile specifies a text file which contains an n by n mask. It has the
    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask

    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to done when applying the mask

    Returns:
    an image which the result of applying the specified mask to src.
    """
    pass

def resize(src: MyImage) -> MyImage:
    """Returns an image which has twice the dimensions of src.

    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image which needs to be resized. 

    Returns:
    an image twice the size of src.
    """
    
    
    
    big_image = MyImage((src.size[0]*2, src.size[1]*2))

    for i in range(src.size[0]):
        for x in range(src.size[1]):
            big_image.set(i*2, x*2,src.get(i,x))

    for i in range(src.size[0]*2):
        for x in range(src.size[1]*2):
            prev_col = src.size[1]*2-1
            prev_row = src.size[0]*2-1

            if (i%2 == 0 and x%2 !=0 and x!= prev_col):
                pixel1 = big_image.get(i,(x-1))
                pixel2 = big_image.get(i,(x+1))
                redavg = (pixel1[0]+pixel2[0])//2
                greenavg = (pixel1[1]+pixel2[1])//2
                blueavg = (pixel1[2]+pixel2[2])//2
                rgbvalue = (redavg,greenavg,blueavg)
                big_image.set(i,x,rgbvalue)
            elif (x==prev_col):
                big_image.set(i,x,big_image.get(i,x-1))

            if(i%2!= 0 and x%2==0 and i != prev_row):
                pixel1 = big_image.get((i-1), x)
                pixel2 = big_image.get((i+1), x)
                redavg = (pixel1[0]+pixel2[0])//2
                greenavg = (pixel1[1]+pixel2[1])//2
                blueavg = (pixel1[2]+pixel2[2])//2
                rgbvalue = (redavg,greenavg,blueavg)
                big_image.set(i,x,rgbvalue)

            elif (x == prev_col):
                big_image.set(i,x,big_image.get(i,x-1))

            if (i%2!= 0 and x%2==0 and i != prev_row and x!= prev_row):
                pixel1=big_image.get((i-1),x)
                pixel2=big_image.get((i+1),x)
                redavg = (pixel1[0] +pixel2[0])//2
                greenavg = (pixel1[1] +pixel2[1])//2
                blueavg = (pixel1[2] +pixel2[2])//2
                
                rgbvalue = (redavg,greenavg,blueavg)
                big_image.set(i,x,rgbvalue)


            elif (i == prev_col):
                big_image.set(i,x,big_image.get(i-1,x))

            if (i%2!=0 and x%2!=0 and i!=prev_row and x!=prev_col):

                
                
                pixel1 = big_image.get((i-1), (x-1))
                pixel2 = big_image.get((i+1), (x+1))
                pixel3 = big_image.get((i+1),(x-1))
                pixel4 = big_image.get((i-1),(x+1))

                redavg = (pixel1[0]+pixel2[0]+pixel3[0]+pixel4[0])//4
                greenavg = (pixel1[1]+pixel2[1]+pixel3[1]+pixel4[1])//4
                blueavg = (pixel1[2]+pixel2[2]+pixel3[2]+pixel4[2])//4
                rgbvalue = (redavg,greenavg,blueavg)

                big_image.set(i,x,rgbvalue)

            elif(i==prev_row and x%2!=0 and x!= prev_col):
                big_image.set(i,x,big_image.get(i-1,x))
            elif(i!=prev_row and i%2!=0 and x== prev_col):
                big_image.set(i,x,big_image.get(i,x-1))
            elif(i==prev_row and x==prev_col):
                big_image.set(i,x,big_image.get(i-1,x-1))
    return big_image
    pass
