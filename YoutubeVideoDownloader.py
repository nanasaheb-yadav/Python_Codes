import pafy

def downloadvideo(url):

    video = pafy.new(url)
    res = video.getbest()
    res.download('/Python_Codes/')


downloadvideo('https://www.youtube.com/watch?v=zWmDLJj999E')