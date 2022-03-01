from digart.transforms.splice import process_images, grid_search, splice_alternate

if __name__ == "__main__":
    # for img1, img2 in grid_search("/Users/robertreilly/code/digital_art/images"):
    #     process_images(img1_path=img1, img2_path=img2, functions=[splice_alternate])
    process_images(
        img1_path="/Users/robertreilly/code/digital_art/images/bean.jpg",
        img2_path="/Users/robertreilly/code/digital_art/images/bkly_bridge.jpg",
        functions=[splice_alternate],
    )
