from .schitem import SchItem

class EESchema(SchItem):
    @classmethod
    def subparse(cls, schpage, tokens, lineiterator):
        cls.checkstate(schpage, -1, 3)
        schpage.page_header = tokens
        tokens = lineiterator.next()
        assert tokens[0].startswith('LIBS:'), line
        schpage.lib_info = tokens

    @staticmethod
    def render(schpage, linelist):
        linelist.append(schpage.page_header.linetext)
        linelist.append(schpage.lib_info.linetext)

class EELAYER(SchItem):
    @classmethod
    def subparse(cls, schpage, tokens, lineiterator):
        cls.checkstate(schpage, 3, 2)
        schpage.eelayer = [tokens]
        for tokens in lineiterator:
            schpage.eelayer.append(tokens)
            if tokens == ['EELAYER', 'END']:
                break

    @staticmethod
    def render(schpage, linelist):
        linelist.extend(x.linetext for x in schpage.eelayer)

class Descr(SchItem):
    keyword = '$Descr'
    @classmethod
    def subparse(cls, schpage, tokens, lineiterator):
        cls.checkstate(schpage, 2, 1)
        schpage.dimx, schpage.dimy = tokens[2:]
        schpage.descr = [tokens]
        for tokens in lineiterator:
            schpage.descr.append(tokens)
            if tokens[0] == '$EndDescr':
                break
        schpage.items = []

    @staticmethod
    def render(schpage, linelist):
        linelist.extend(x.linetext for x in schpage.descr)

class EndSCHEMATC(SchItem):
    keyword = '$EndSCHEMATC'
    @classmethod
    def subparse(cls, schpage, tokens, lineiterator):
        cls.checkstate(schpage, 1, 0)

    @classmethod
    def render(cls, schpage, linelist):
        linelist.append(cls.keyword)
