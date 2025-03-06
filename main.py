import flet as ft

def page02(e):
    
    def clearvalue(e: ft.OnFocusEvent):
        searchbar.controls[0].value=''
        searchbar.update()
        
    def xmarkstate(e):
        if searchbar.controls[0].value=='':
            searchbar.controls[0].value = '무엇을 찾고 계신가요?'
            searchbar.controls[1].visible=False
        else:
            searchbar.controls[1].visible=True
        searchbar.update()
        
    def clearSearchBar(e):
        searchbar.controls[0].value = '무엇을 찾고 계신가요?'
        searchbar.controls[1].visible=False
        searchbar.update()
        
    def suggest_item_maker():
        imgRowsinput = []
        for j in range(15):
            imgRows = ft.Row(controls=[],width=450,spacing=15)
            for i in range(0, 2):
                if i%2==0:
                    imgRows.controls.append(
                        ft.Container(margin=ft.Margin(bottom=20,top=0,left=0,right=0),content=ft.Column(controls=[ft.Image(
                            src=f"https://picsum.photos/200/200?{10*j+i}",
                            width=190,
                            height=300,
                            fit=ft.ImageFit.FIT_HEIGHT,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(2),
                        ),ft.Row([ft.Text(f'소품: {format(10*j+1,"04")}\n₩ {10000*j+i*1000+100}',color='#000000',size=10),
                                  ft.IconButton(icon=ft.CupertinoIcons.BOOKMARK,icon_color='#000000',icon_size=15)],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=190)
                        ])
                    ))
                elif i%2==1:
                    imgRows.controls.append(
                        ft.Container(margin=ft.Margin(bottom=20,top=0,left=0,right=0),content=ft.Column(controls=[ft.Image(
                            src=f"https://picsum.photos/200/200?{10*j+i}",
                            width=190,
                            height=300,
                            fit=ft.ImageFit.FIT_HEIGHT,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(2),
                        ),ft.Row([ft.Text(f'소품: {format(10*j+1,"04")}\n₩ {10000*j+i*1000+100}',color='#000000',size=10),
                                  ft.IconButton(icon=ft.CupertinoIcons.BOOKMARK,icon_color='#000000',icon_size=15)],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=190)
                        ])
                    ))
            imgRowsinput.append(imgRows)
        imgRowsinput.insert(0,ft.Text('추천 아이템',color='#000000'))
        suggest = ft.Column(controls=imgRowsinput)
        return suggest
    
    
    emptyContainer1 = ft.Container(width=600,height=80)
    emptyContainer2 = ft.Container(width=600,height=130)
        
    mainbutton = ft.Column(controls=[emptyContainer1,ft.Row(wrap=True,tight=True,controls=[
        ft.TextButton(text='여성',on_click=lambda e: print('woman'),style=ft.ButtonStyle(color='#000000'),scale=.8),
        ft.TextButton(text='남성',on_click=lambda e: print('man'),style=ft.ButtonStyle(color='#000000'),scale=.8),
        ft.TextButton(text='어린이',on_click=lambda e: print('child'),style=ft.ButtonStyle(color='#000000'),scale=.8),
        ft.TextButton(text='HOME',on_click=lambda e: print('home'),style=ft.ButtonStyle(color='#000000'),scale=.8),
    ])])
    
    
    searchbar = ft.Row(controls=[
        ft.TextField(width=350,hint_text='무엇을 찾고 계신가요?',value='무엇을 찾고 계신가요?',border_width=0,on_change=xmarkstate,on_focus=clearvalue,text_align=ft.TextAlign.CENTER,focus_color='#ffffff',color='#000000',focused_border_color='#ffffff',border_color='#f1f1f1',cursor_color='#000000'),
        ft.IconButton(icon=ft.CupertinoIcons.XMARK,icon_color='#000000',visible=False,on_click=clearSearchBar)
    ],wrap=True)
    
    
    
    image_group = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.ADAPTIVE,height=800,width=600,controls=[emptyContainer1,
        
        emptyContainer2,
        ft.Column(controls=[searchbar,ft.Divider(trailing_indent=50,leading_indent=50,color='#f1f1f1')]),
        emptyContainer2,suggest_item_maker()
        
        
        
    ])
    return ft.Stack(controls=[image_group,mainbutton],alignment=ft.alignment.top_center)
def page03(e):
    maintitle = ft.Text(value='MOLA',size=150,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=-31),text_align=ft.TextAlign.CENTER)
    heukitosuni = ft.Text(value='THE 흑히와토수니',size=30,color='#000000')
    
    return ft.Column([maintitle,heukitosuni],spacing=50)
def page04(e):
    maintitle = ft.Text(value='ZALA',size=150,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=-31),text_align=ft.TextAlign.CENTER)
    taewoongBBu = ft.Text(value='THE 태웅이뿌',size=30,color='#000000')
    
    return ft.Column([maintitle,taewoongBBu],spacing=50)

def page05(e):
    maintitle = ft.Text(value='MUNG',size=150,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=-31),text_align=ft.TextAlign.CENTER)
    mungjaMichi=ft.Text(value='THE 엄뭉자 ❤️ 믹히',size=30,color='#000000')
    mungBBung = ft.Image(src='./mungbbung.png',width=380,fit=ft.ImageFit.FIT_WIDTH)
    return ft.Column([maintitle,mungjaMichi,mungBBung],spacing=50)

def page01(e):
    
    def movieplay(e:ft.OnScrollEvent):
        print(e.scroll_delta)
        emptyContainer3.content = movie
        emptyContainer3.update()
    
    maintitle = ft.Text(value='ZARA',size=150,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=-31),text_align=ft.TextAlign.CENTER)
    mainimage = ft.Container(content=ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/test.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay90ZXN0LnBuZyIsImlhdCI6MTc0MTAzMDYzOCwiZXhwIjoxNzcyNTY2NjM4fQ.nw4Lnfa0tQmuG_sFOZwBWXVCfZ72i04jXZiPLF9o7P8',fit=ft.ImageFit.FIT_WIDTH),width=380)
    contentDescription1 = ft.Container(width=400,content=ft.Column(spacing=2,horizontal_alignment=ft.CrossAxisAlignment.END,controls=[
        ft.Text(value='THE SUMMER EDITION',size=15,color='#000000'),
        ft.Text(value='WITH',size=15,color='#000000'),
        ft.Text(value='LEMON',size=15,color='#000000'),
    ]))
    
    contentDescription2 = ft.Container(width=400,content=ft.Column(spacing=2,horizontal_alignment=ft.CrossAxisAlignment.END,controls=[
        ft.Text(value='JOIN LIFE',size=15,color='#000000'),

    ]))
    
    contentDescription3 = ft.Container(width=400,content=ft.Column(spacing=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
        ft.Text(value='뉴스레터 등록',size=12,color='#000000'),

    ]))
    
    contentDescription4 = ft.Container(width=400,content=ft.Column(spacing=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
        ft.Text(value='아이티엑스코리아 유한회사 ｜ 사업자등록번호: 120-88-14733 ｜ 대표자 : ROMAY DE LA COLINA JOSE MANUEL ｜ 서울시 강남구 영동대로 511 (삼성동, 트레이드타워 33층) ｜ 대표번호: 080-479-0880 ｜ 호스팅 서비스 사업자: ITX MERKEN, B.V.｜ 통신판매업신고 : 제2014-서울강남-02297 (사업자정보확인) | 지급보증안내',size=10,color='#000000'),

    ]))
    
    contentDescription5 = ft.Container(width=400,content=ft.Column(spacing=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
        ft.Text(value='개인정보처리방침 | 구매 조건',size=12,color='#000000'),

    ]))
    
    movie = ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/output.gif?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9vdXRwdXQuZ2lmIiwiaWF0IjoxNzQxMDMxNzAyLCJleHAiOjE3NzI1Njc3MDJ9._3Zn-FZbCRXi-pp8V7_scoaPMes4Vxcb0i41Bn9CISI',fit=ft.ImageFit.FIT_WIDTH,width=300)
    # movie = ft.Video(playlist=[ft.VideoMedia('https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/output.gif?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9vdXRwdXQuZ2lmIiwiaWF0IjoxNzQxMDMxNzAyLCJleHAiOjE3NzI1Njc3MDJ9._3Zn-FZbCRXi-pp8V7_scoaPMes4Vxcb0i41Bn9CISI')],playlist_mode=ft.PlaylistMode.LOOP,show_controls=False,autoplay=True,muted=True,expand=True,fit=ft.ImageFit.FIT_WIDTH,width=380)
    emptyContainer1 = ft.Container(width=600,height=250)
    emptyContainer2 = ft.Container(width=600,height=400)
    emptyContainer22 = ft.Container(width=600,height=200)
    emptyContainer23 = ft.Container(width=600,height=50)
    emptyContainer3 = ft.Container(width=400,height=500)

    con = ft.Column(scroll=ft.ScrollMode.ADAPTIVE,height=800,width=600,on_scroll=movieplay,alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[
        emptyContainer1,mainimage,contentDescription1,emptyContainer2,emptyContainer3,contentDescription2,emptyContainer2,emptyContainer2,contentDescription3,emptyContainer22,contentDescription4,emptyContainer23,contentDescription5
    ])
    res = ft.Stack([con,maintitle],alignment=ft.alignment.top_center)
    return res

        
def main(page: ft.Page):
    def pageChange(e):
        try:
            page.controls.pop(-1)
        except:
            pass
        print(e.control.selected_index)
        if e.control.selected_index==0:
            page.add(page01(e))
            page.update()
        elif e.control.selected_index==1:
            page.add(page02(e))
            page.update()
            
        elif e.control.selected_index==2:
            page.add(page03(e))
            page.update()
            
        elif e.control.selected_index==3:
            page.add(page04(e))
            page.update()
            
        elif e.control.selected_index==4:
            page.add(page05(e))
            page.update()
            
    page.bgcolor='#ffffff'
    page.title = "CupertinoNavigationBar Example"
    # page.window_width = 720
    # page.window_height = 1280
    # page.window_resizable = False  # 창 크기 고정 (선택 사항)

    # 화면 가운데 정렬
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.fonts={'zaramain':'https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/OPTIBodoni-Antiqua.otf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9PUFRJQm9kb25pLUFudGlxdWEub3RmIiwiaWF0IjoxNzQwOTkxMDM0LCJleHAiOjE3NzI1MjcwMzR9.BYxXY6vXOOoyk_L1xudbJzfy42bRI90WtWzFfGOJDcY'}
    # page.fonts={'Stencil':'/Users/julimpark/Library/Fonts/STENCIL.TTF'}
    page.navigation_bar = ft.CupertinoNavigationBar(selected_index=0,
        bgcolor=ft.Colors.WHITE,
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        on_change=pageChange,
        destinations=[
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.HOUSE_ALT, label=''),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.SEARCH, label=''),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.BOOKMARK,label="메뉴"),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.BAG),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.PERSON),
            
        ]
    )
    page.add(page01(''))
    page.update()
    # page.add(ft.SafeArea(ft.Text("Body!")))


ft.app(main, view=ft.AppView.WEB_BROWSER)
