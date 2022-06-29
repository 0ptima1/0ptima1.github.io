import os
import yaml
import argparse
from pdf2image import convert_from_path
from datetime import datetime


def load_pdf():
    slides = convert_from_path(args['pdf_path'], dpi=600)
    for idx_slide, slide in enumerate(slides):
        slide.save(f"{args['img_path']}/{idx_slide}.jpg", "JPEG")
    print("Success : PDF --> IMG")


def get_fm(file, title, desc, idx_cover_page: int):
    file.write('---\n')
    file.write('layout: post\n')
    file.write(f"title: {title}\n")
    file.write(f"description: {desc}\n")
    file.write(f"image : {args['img_path']}/{idx_cover_page}.jpg\n")
    file.write('nav-menu:false\n')
    file.write('---\n')
    return file


def get_body(file):
    for img in os.listdir(args['img_path']):
        file.write(f'<span class="image fit"><img src="{{% link {args["img_path"]}/{img} %}}" alt="" /></span>')
    return file


def write_post():
    with open(args['post_path'], 'w', encoding='utf-8') as md:
        md = get_fm(md, args['file_name'], args['file_desc'], 0)
        md = get_body(md)
    print("Success : IMG --> MD")

def get_today():
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day

    return f"{year}-{month}-{day}"


def main():
    # print(args)
    load_pdf()
    write_post()


if __name__ == '__main__':
    dir_root = os.getcwd()
    with open('./pdf_config.yaml', encoding='utf-8') as f:
        args = yaml.safe_load(f)
    # parser = argparse.ArgumentParser(description="발표자료를 포스트로 생성합니다.")
    # parser.add_argument("--file_name", required=True, help="발표자료명")
    # parser.add_argument("--file_desc", required=True, help="발표3줄요약")
    # args = vars(parser.parse_args())

    pdf_path = f"{dir_root}/assets/pdfs/{args['file_name']}.pdf"
    img_path = f"assets/images/ppt/{args['file_name']}"
    post_path = f"{dir_root}/_posts/{get_today()}-{args['file_name']}.md"
    args['pdf_path'] = pdf_path
    args['img_path'] = img_path
    args['post_path'] = post_path

    try:
        os.makedirs(f"assets/images/ppt/{args['file_name']}")
    except FileExistsError:
        print("Directory exists!")

    main()
