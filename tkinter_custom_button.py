def hover(btn,c="#24a0ed"):
    def on_leave_download(e):
        btn['background'] = c
    def on_enter_download(e):
        btn['background'] = 'lightblue'
    btn.bind("<Enter>", on_enter_download)
    btn.bind("<Leave>", on_leave_download)
