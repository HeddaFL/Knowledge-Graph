from rdflib import Namespace, Literal, Graph, BNode
from rdflib.namespace import RDF, FOAF, XSD
from rdflib.collection import Collection

g = Graph()
ex = Namespace('http://example.org/')
g.bind('ex', ex)
g.bind('foaf', FOAF)

#Info about the show:
g.add((ex.TheKardashians, RDF.type, FOAF.Project))
g.add((ex.TheKardashians, FOAF.name, Literal('The Kardashians')))
g.add((ex.TheKardashians, ex.isOn, ex.DisneyPlus))

#Who is on the show?
g.add((ex.KrisJenner, RDF.type, FOAF.Person))
g.add((ex.KrisJenner, FOAF.name, Literal('Kris Jenner')))
g.add((ex.KrisJenner, FOAF.nick, Literal('Momager')))
g.add((ex.KrisJenner, ex.isOnShow, ex.TheKardashians))

g.add((ex.KourtneyKardashian, RDF.type, FOAF.Person))
g.add((ex.KourtneyKardashian, FOAF.name, Literal('Kourtney Kardashian')))
g.add((ex.KourtneyKardashian, ex.isOnShow, ex.TheKardashians))

g.add((ex.KimKardashian, RDF.type, FOAF.Person))
g.add((ex.KimKardashian, FOAF.name, Literal('Kim Kardashian')))
g.add((ex.KimKardashian, ex.isOnShow, ex.TheKardashians))

g.add((ex.KhloeKardashian, RDF.type, FOAF.Person))
g.add((ex.KhloeKardashian, FOAF.name, Literal('Khloe Kardashian')))
g.add((ex.KhloeKardashian, ex.isOnShow, ex.TheKardashians))

g.add((ex.KendallJenner, RDF.type, FOAF.Person))
g.add((ex.KendallJenner, FOAF.name, Literal('Kendall Jenner')))
g.add((ex.KendallJenner, ex.isOnShow, ex.TheKardashians))

g.add((ex.KylieJenner, RDF.type, FOAF.Person))
g.add((ex.KylieJenner, FOAF.name, Literal('Kendall Jenner')))
g.add((ex.KylieJenner, ex.isOnShow, ex.TheKardashians))

g.add((ex.ScottDisick, RDF.type, FOAF.Person))
g.add((ex.ScottDisick, FOAF.name, Literal('Scott Disick')))
g.add((ex.ScottDisick, ex.isOnShow, ex.TheKardashians))

#Relations: 
g.add((ex.KrisJenner, ex.exPartner, ex.RobertGeorgeKardashian))
g.add((ex.KrisJenner, ex.exPartner, ex.WilliamBruceJenner))
g.add((ex.KrisJenner, ex.currentPartner, ex.CoreyGamble))
g.add((ex.KrisJenner, ex.motherOf, ex.KourtneyKardashian))
g.add((ex.KrisJenner, ex.motherOf, ex.KimKardashian))
g.add((ex.KrisJenner, ex.motherOf, ex.KhloeKardashian))
g.add((ex.KrisJenner, ex.motherOf, ex.RobertKardashian))
g.add((ex.KrisJenner, ex.motherOf, ex.KendallJenner))
g.add((ex.KrisJenner, ex.motherOf, ex.KylieJenner))

g.add((ex.RobertGeorgeKardashian, RDF.type, FOAF.Person))
g.add((ex.RobertGeorgeKardashian, FOAF.name, Literal('Robert George Kardashian')))
g.add((ex.RobertGeorgeKardashian, ex.fatherOf, ex.KourtneyKardashian))
g.add((ex.RobertGeorgeKardashian, ex.fatherOf, ex.KimKardashian))
g.add((ex.RobertGeorgeKardashian, ex.fatherOf, ex.KhloeKardashian))
g.add((ex.RobertGeorgeKardashian, ex.fatherOf, ex.RobertKardashian))

g.add((ex.KourtneyKardashian, ex.exPartner, ex.ScottDisick))
g.add((ex.KourtneyKardashian, ex.currentPartner, ex.TravisBarker))
g.add((ex.KourtneyKardashian, ex.motherOf, ex.MasonDashDisick))
g.add((ex.KourtneyKardashian, ex.motherOf, ex.PenelopeScotlandDisick))
g.add((ex.KourtneyKardashian, ex.motherOf, ex.ReignAstonDisick))
g.add((ex.KourtneyKardashian, ex.motherOf, ex.RockyThirteenBarker))
g.add((ex.KourtneyKardashian, ex.stepMotherOf, ex.LandonBarker))
g.add((ex.KourtneyKardashian, ex.stepMotherOf, ex.AlabamaBarker))

g.add((ex.ScottDisick, ex.fatherOf, ex.MasonDashDisick))
g.add((ex.ScottDisick, ex.fatherOf, ex.PenelopeScotlandDisick))
g.add((ex.ScottDisick, ex.fatherOf, ex.ReignAstonDisick))

g.add((ex.TravisBarker, RDF.type, FOAF.Person))
g.add((ex.TravisBarker, FOAF.name, Literal('Travis Barker')))
g.add((ex.TravisBarker, ex.exPartner, ex.ShannaMoakler))
g.add((ex.TravisBarker, ex.fatherOf, ex.LandonBarker))
g.add((ex.TravisBarker, ex.fatherOf, ex.AlabamaBarker))
g.add((ex.TravisBarker, ex.fatherOf, ex.RockyThirteenBarker))
g.add((ex.TravisBarker, ex.stepFatherOf, ex.MasonDashDisick))
g.add((ex.TravisBarker, ex.stepFatherOf, ex.PenelopeScotlandDisick))
g.add((ex.TravisBarker, ex.stepFatherOf, ex.ReignAstonDisick))

g.add((ex.ShannaMoakler, RDF.type, FOAF.Person))
g.add((ex.ShannaMoakler, FOAF.name, Literal('Shanna Moakler')))
g.add((ex.ShannaMoakler, ex.motherOf, ex.LandonBarker))
g.add((ex.ShannaMoakler, ex.motherOf, ex.AlabamaBarker))

g.add((ex.KimKardashian, ex.exPartner, ex.ReggieBush))
g.add((ex.KimKardashian, ex.exPartner, ex.KrisHumphries))
g.add((ex.KimKardashian, ex.exPartner, ex.KanyeWest))
g.add((ex.KimKardashian, ex.motherOf, ex.NorthWest))
g.add((ex.KimKardashian, ex.motherOf, ex.SaintWest))
g.add((ex.KimKardashian, ex.motherOf, ex.ChicagoWest))
g.add((ex.KimKardashian, ex.motherOf, ex.PsalmWest))

g.add((ex.KanyeWest, RDF.type, FOAF.Person))
g.add((ex.KanyeWest, FOAF.name, Literal('Kanye West')))
g.add((ex.KanyeWest, ex.currentPartner, ex.BiancaCensori))
g.add((ex.KanyeWest, ex.fatherOf, ex.NorthWest))
g.add((ex.KanyeWest, ex.fatherOf, ex.SaintWest))
g.add((ex.KanyeWest, ex.fatherOf, ex.ChicagoWest))
g.add((ex.KanyeWest, ex.fatherOf, ex.PsalmWest))

g.add((ex.KhloeKardashian, ex.exPartner, ex.LamarOdom))
g.add((ex.KhloeKardashian, ex.exPartner, ex.TristanThompson))
g.add((ex.KhloeKardashian, ex.motherOf, ex.TrueThompson))
g.add((ex.KhloeKardashian, ex.motherOf, ex.TatumThompson))

g.add((ex.LamarOdom, RDF.type, FOAF.Person))
g.add((ex.LamarOdom, FOAF.name, Literal('Lamar Odom')))

g.add((ex.TristanThompson, RDF.type, FOAF.Person))
g.add((ex.TristanThompson, FOAF.name, Literal('Tristan Thompson')))
g.add((ex.TristanThompson, ex.fatherOf, ex.TrueThompson))
g.add((ex.TristanThompson, ex.fatherOf, ex.TatumThompson))
g.add((ex.TristanThompson, ex.fatherOf, ex.PrinceOliverThompson))
g.add((ex.TristanThompson, ex.fatherOf, ex.TheoThompson))

g.add((ex.RobertKardashian, ex.exPartner, ex.BlacChyna))
g.add((ex.RobertKardashian, ex.fatherOf, ex.DreamKardashian))

g.add((ex.BlacChyna, RDF.type, FOAF.Person))
g.add((ex.BlacChyna, FOAF.name, Literal('Blac Chyna')))
g.add((ex.BlacChyna, ex.motherOf, ex.DreamKardashian))
g.add((ex.BlacChyna, ex.motherOf, ex.KingCairo))
g.add((ex.BlacChyna, ex.exPartner, ex.Tyga))

g.add((ex.Tyga, RDF.type, FOAF.Person))
g.add((ex.Tyga, FOAF.name, Literal('Tyga')))
g.add((ex.Tyga, ex.fatherOf, ex.KingCairo))

g.add((ex.WilliamBruceJenner, RDF.type, FOAF.Person))
g.add((ex.WilliamBruceJenner, FOAF.name, Literal('Caitlyn Jenner')))
g.add((ex.WilliamBruceJenner, ex.fatherOf, ex.KendallJenner))
g.add((ex.WilliamBruceJenner, ex.fatherOf, ex.KylieJenner))

g.add((ex.KendallJenner, ex.exPartner,ex.HarryStyles))
g.add((ex.KendallJenner, ex.exPartner, ex.BenSimmons))
g.add((ex.KendallJenner, ex.currentPartner, ex.BadBunny))

g.add((ex.KylieJenner, ex.exPartner, ex.Tyga))
g.add((ex.KylieJenner, ex.exPartner, ex.TravisScott))
g.add((ex.KylieJenner, ex.currentPartner, ex.TimotheeChalamet))
g.add((ex.KylieJenner, ex.motherOf, ex.StormiWebster))
g.add((ex.KylieJenner, ex.motherOf, ex.AireWebster))

g.add((ex.TravisScott, RDF.type, FOAF.Person))
g.add((ex.TravisScott, FOAF.name, Literal('Travis Scott')))
g.add((ex.TravisScott, ex.fatherOf, ex.StormiWebster))
g.add((ex.TravisScott, ex.fatherOf, ex.AireWebster))

#Different shows that also featured the Kardashians/Jenners:
g.add((ex.KeepingUpWithTheKardashians, RDF.type, FOAF.pastProject))
g.add((ex.KeepingUpWithTheKardashians, FOAF.name, Literal('Keeping up with the Kardashians')))
g.add((ex.KourtneyKardashian, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KimKardashian, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KhloeKardashian, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.RobertKardashian, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KendallJenner, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KylieJenner, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KrisJenner, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.WilliamBruceJenner, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.KanyeWest, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.ScottDisick, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.Tyga, ex.wasOn, ex.KeepingUpWithTheKardashians))
g.add((ex.BlacChyna, ex.wasOn, ex.KeepingUpWithTheKardashians))

g.add((ex.KourtneyAndKhloeTakeTheHamptons, RDF.type, FOAF.pastProject))
g.add((ex.KourtneyAndKhloeTakeTheHamptons, FOAF.name, Literal('Kourtney and Khloe take the Hamptons')))
g.add((ex.KourtneyKardashian, ex.wasOn, ex.KourtneyAndKhloeTakeTheHamptons))
g.add((ex.KhloeKardashian, ex.wasOn, ex.KourtneyAndKhloeTakeTheHamptons))
g.add((ex.ScottDisick, ex.wasOn, ex.KourtneyAndKhloeTakeTheHamptons))

g.add((ex.KourtneyAndKhloeTakeMiami, RDF.type, FOAF.pastProject))
g.add((ex.KourtneyAndKhloeTakeMiami, FOAF.name, Literal('Kourtney and Khloe take Miami')))
g.add((ex.KourtneyKardashian, ex.wasOn, ex.KourtneyAndKhloeTakeMiami))
g.add((ex.KhloeKardashian, ex.wasOn, ex.KourtneyAndKhloeTakeMiami))
g.add((ex.ScottDisick, ex.wasOn, ex.KourtneyAndKhloeTakeMiami))

g.add((ex.KourtneyAndKimTakeNewYork, RDF.type, FOAF.pastProject))
g.add((ex.KourtneyAndKimTakeNewYork, FOAF.name, Literal('Kourtney and Kim take New York')))
g.add((ex.KourtneyKardashian, ex.wasOn, ex.KourtneyAndKimTakeNewYork))
g.add((ex.KimKardashian, ex.wasOn, ex.KourtneyAndKimTakeNewYork))
g.add((ex.ScottDisick, ex.wasOn, ex.KourtneyAndKimTakeNewYork))
g.add((ex.KrisHumphries, ex.wasOn, ex.KourtneyAndKimTakeNewYork))

g.add((ex.KhloeAndLamar, RDF.type, FOAF.pastProject))
g.add((ex.KhloeAndLamar, FOAF.name, Literal('Khloe and Lamar')))
g.add((ex.KhloeKardashian, ex.wasOn, ex.KhloeAndLamar))
g.add((ex.LamarOdom, ex.wasOn, ex.KhloeAndLamar))

g.add((ex.RobAndChyna, RDF.type, FOAF.pastProject))
g.add((ex.RobAndChyna, FOAF.name, Literal('Rob and Chyna')))
g.add((ex.RobertKardashian, ex.wasOn, ex.RobAndChyna))
g.add((ex.BlacChyna, ex.wasOn, ex.RobAndChyna))

g.add((ex.RevengeBody, RDF.type, FOAF.pastProject))
g.add((ex.RevengeBody, FOAF.name, Literal('Revenge Body with Khloe Kardashian')))
g.add((ex.KhloeKardashian, ex.wasOn, ex.RevengeBody))

#BNode examples
SeveralBusinesses = BNode()
g.add((SeveralBusinesses, ex.ownedBy, ex.KrisJenner))
g.add((SeveralBusinesses, ex.name, Literal('Several Businesses owned by Kris Jenner')))

Address1 = BNode()
g.add((Address1, ex.ownedBy, ex.KimKardashian))
g.add((Address1, ex.name, Literal('Address 1')))

Address2 = BNode()
g.add((Address2, ex.ownedBy, ex.KimKardashian))
g.add((Address2, ex.name, Literal('Address 2')))

#Ages: 
g.add((ex.KrisJenner, ex.age, Literal(68, datatype=XSD.integer)))
g.add((ex.KourtneyKardashian, ex.age, Literal(44, datatype=XSD.integer)))
g.add((ex.KimKardashian, ex.age, Literal(43, datatype=XSD.integer)))
g.add((ex.KhloeKardashian, ex.age, Literal(39, datatype=XSD.integer)))
g.add((ex.RobertKardashian, ex.age, Literal(36, datatype=XSD.integer)))
g.add((ex.KendallJenner, ex.age, Literal(28, datatype=XSD.integer)))
g.add((ex.KylieJenner, ex.age, Literal(26, datatype=XSD.integer)))

#3 generation: 
g.add((ex.KrisJenner, ex.grandMotherOf, ex.MasonDashDisick))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.PenelopeScotlandDisick))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.ReignAstonDisick))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.RockyThirteenBarker))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.NorthWest))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.SaintWest))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.ChicagoWest))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.PsalmWest))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.TrueThompson))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.TatumThompson))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.DreamKardashian))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.StormiWebster))
g.add((ex.KrisJenner, ex.grandMotherOf, ex.AireWebster))

TheKardashianClanKids = BNode()
Collection(g, TheKardashianClanKids, [ex.MasonDashDisick, ex.PenelopeScotlandDisick,
                                  ex.ReignAstonDisick, ex.RockyThirteenBarker, ex.NorthWest, ex.SaintWest,
                                  ex.ChicagoWest, ex.PsalmWest, ex.TrueThompson, ex.TatumThompson,
                                  ex.DreamKardashian, ex.StormiWebster, ex.AireWebster])

g.add((ex.TheKardashians, ex.theseKidsAreCousins, TheKardashianClanKids))

#Find all of Kris Jenners Grandkids:
for s, p, o in g.triples((ex.KrisJenner, ex.grandMotherOf, None)):
    print(f'All of Kris Jenners grandkids: {o}')

#Find everybody that is a father: 
for sub, obj, in g[ : ex.fatherOf :]:
    print(f'{sub} is {ex.fatherOf} to {obj}')

#Method that can submit the model for rendering and save the returned image to file. 
import requests
import shutil

def graph_to_image(input):
    data = {'rdf': input, 'from':'ttl', 'to':'png'}
    link = 'https://www.ldf.fi/service/rdf-grapher'
    response = requests.get(link, params = data, stream = True)
    print(response.raw)

    with open('TheKardashians.png', 'wb') as file:
        shutil.copyfileobj(response.raw, file)

#Save to computer:
g.serialize(destination = 'TheKardashians_ttl', format='ttl')
g.parse(location = 'TheKardashians_ttl', format='ttl')


