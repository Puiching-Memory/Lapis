import win32clipboard

def get_clipboard_html():
    # https://learn.microsoft.com/zh-cn/windows/win32/dataxchg/clipboard-formats
    try:
        # 打开剪贴板
        win32clipboard.OpenClipboard()

        # 获取HTML格式的ID
        CF_HTML = win32clipboard.RegisterClipboardFormat("HTML Format")

        # 获取剪贴板中的数据
        data = win32clipboard.GetClipboardData(CF_HTML)
        return data
    except Exception as e:
        print(e)
    finally:
        # 关闭剪贴板
        win32clipboard.CloseClipboard()

if __name__ == '__main__':
    # 从剪贴板中读取文本
    clipboard_text = get_clipboard_html()
    print("剪贴板中的文本是：", clipboard_text)
