from django.core.management.base import BaseCommand
from antibiyogram.models import MikroorganizmaKategorisi,Mikroorganizma,Antibiyotik

ANTIBIYOTIKLER = {
    "AMK" : "amikacin",
    "CEFTRX" : "ceftriaxone",
    "FLUCY" : "flucytosine",
    "OX" : "oxacillin",
    "AMP" : "ampicillin",
    "CEFUR" : "cefuroxime",
    "GENT" : "gentamicin",
    "PB" : "polymyxin B",
    "AMPSUL" : "ampicillin / sulbactam",
    "CTET" : "cefotetan",
    "GENTHL" : "gentamicin – high level test",
    "PIP" : "piperacillin",
    "AMXCLV" : "amoxicillin / clavulanic acid",
    "CIPRO" : "ciprofloxacin",
    "IMI" : "imipenem",
    "PIPTAZ" : "piperacillin / tazobactam",
    "ANID" : "anidulafungin",
    "CLIND" : "clindamycin",
    "ITRA" : "itraconazole",
    "RIF" : "rifampin",
    "AZT" : "aztreonam",
    "COL" : "colistin",
    "LEVO" : "levofloxacin",
    "TETRA" : "tetracycline",
    "CASPO" : "caspofungin",
    "DAPTO" : "daptomycin",
    "LNZ" : "linezolid",
    "TIG" : "tigecycline",
    "CEFAZ" : "cefazolin",
    "DORI" : "doripenem",
    "MERO" : "meropenem",
    "TMZ" : "trimethoprim / sulfamethoxazole",
    "CEFEP" : "cefepime",
    "DOXY" : "doxycycline",
    "METH" : "methicillin",
    "TOBRA" : "tobramycin",
    "CEFOT" : "cefotaxime",
    "ERTA" : "ertapenem",
    "MICA" : "micafungin",
    "VANC" : "vancomycin",
    "CEFOX" : "cefoxitin",
    "ERYTH" : "erythromycin",
    "MINO" : "minocycline",
    "VORI" : "voriconazole",
    "CEFTAZ" : "ceftazidime",
    "FLUCO" : "fluconazole",
    "MOXI" : "moxifloxacin",
}

KATEGORILER = [
    "Gram Pozitif",
    "Gram Negatif",
    "Mantar",
]

MIKROORGANIZMALAR = {
    'Staphylococcus coagulase-negative' : {
        'category' : 'Gram Pozitif',
        'ab': ['VANC'],
    },
    'Enterococcus faecium' : {
        'category' : 'Gram Pozitif',
        'ab': ['DAPTO','GENTHL','LNZ','VANC'],
    },
    'Enterococcus faecalis' : {
        'category' : 'Gram Pozitif',
        'ab': ['DAPTO','GENTHL','LNZ','VANC'],
    },
    'Enterococcus spp.' : {
        'category' : 'Gram Pozitif',
        'ab': ['DAPTO','GENTHL','LNZ','VANC'],
    },
    'Staphylococcus aureus' : {
        'category' : 'Gram Pozitif',
        'ab': ['CIPRO','LEVO','MOXI','CLIND','DAPTO','DOXY','MINO','ERYTH','GENT','LNZ','OX','CEFOX','METH','RIF','TETRA','TIG','TMZ','VANC',],
    },
    'Acinetobacter' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK', 'AMPSUL', 'AZT', 'CEFEP', 'CEFTAZ', 'CIPRO', 'LEVO', 'COL', 'PB', 'GENT', 'IMI', 'MERO', 'DORI',
            'PIP', 'PIPTAZ', 'TETRA', 'DOXY', 'MINO', 'TMZ', 'TOBRA'
        ],
    },
    'Escherichia coli' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK','AMP','AMPSUL','AMXCLV','AZT','CEFAZ','CEFEP','CEFOT','CEFTRX','CEFTAZ','CEFUR','CEFOX','CTET','CIPRO','LEVO','MOXI','COL','PB','ERTA','GENT','IMI','MERO','DORI','PIPTAZ','TETRA','DOXY','MINO','TIG','TMZ','TOBRA'
        ],
    },
    'Enterobacter' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK','AMP','AMPSUL','AMXCLV','AZT','CEFAZ','CEFEP','CEFOT','CEFTRX','CEFTAZ','CEFUR','CEFOX','CTET','CIPRO','LEVO','MOXI','COL','PB','ERTA','GENT','IMI','MERO','DORI','PIPTAZ','TETRA','DOXY','MINO','TIG','TMZ','TOBRA'
        ],
    },
    'Klebsiella pneumonia' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK','AMP','AMPSUL','AMXCLV','AZT','CEFAZ','CEFEP','CEFOT','CEFTRX','CEFTAZ','CEFUR','CEFOX','CTET','CIPRO','LEVO','MOXI','COL','PB','ERTA','GENT','IMI','MERO','DORI','PIPTAZ','TETRA','DOXY','MINO','TIG','TMZ','TOBRA'
        ],
    },
    'Klebsiella oxytoca' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK','AMP','AMPSUL','AMXCLV','AZT','CEFAZ','CEFEP','CEFOT','CEFTRX','CEFTAZ','CEFUR','CEFOX','CTET','CIPRO','LEVO','MOXI','COL','PB','ERTA','GENT','IMI','MERO','DORI','PIPTAZ','TETRA','DOXY','MINO','TIG','TMZ','TOBRA'
        ],
    },
    'Pseudomonas aeruginosa' : {
        'category' : 'Gram Negatif',
        'ab': [
            'AMK','AZT','CEFEP','CEFTAZ','CIPRO','LEVO','COL','PB','GENT','IMI','MERO','DORI','PIP','PIPTAZ','TOBRA'
        ],
    },
    'Candida' : {
        'category' : 'Mantar',
        'ab': [
            'ANID','CASPO','FLUCO','FLUCY','ITRA','MICA','VORI'
        ],
    },
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.add_antibiyotikler()
        self.add_kategoriler()
        self.add_mikroorganizmalar()

    def add_antibiyotikler(self):
        for k,v in ANTIBIYOTIKLER.items():
            ab,created = Antibiyotik.objects.get_or_create(ad=k)
            if created:
                ab.uzun_ad = v
                ab.save()

    def add_kategoriler(self):
        for kat in KATEGORILER:
            MikroorganizmaKategorisi.objects.get_or_create(ad=kat)

    def add_mikroorganizmalar(self):
        for k in MIKROORGANIZMALAR:
            v = MIKROORGANIZMALAR[k]
            kategori = MikroorganizmaKategorisi.objects.get(ad=v['category'])
            try:
                mikrop = Mikroorganizma.objects.get(ad=k)
            except:
                mikrop = Mikroorganizma.objects.create(ad=k,kategori=kategori)

            if not mikrop.kategori == kategori:
                mikrop.kategori = kategori
                mikrop.save()

            for ab in v['ab']:
                antibiyotik = Antibiyotik.objects.get(ad=ab)
                if not mikrop.antibiyotikler.filter(id=antibiyotik.id).exists():
                    mikrop.antibiyotikler.add(antibiyotik)

