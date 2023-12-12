def address(ipfind, liste_IP):
    for ip in liste_IP:
        if ip==ipfind:
            return liste_IP, print("Trouvée")
    liste_IP.append(ipfind)
    return liste_IP, print("Pas trouvée, ajoutée")

liste_IP=[[192,168,10,1],[192,168,10,25],[192,168,10,13]]

liste_IP=address([192,168,10,12], liste_IP)[0]
liste_IP=address([192,168,10,12], liste_IP)[0]
liste_IP=address([192,168,10,13], liste_IP)[0]
liste_IP=address([192,168,10,18], liste_IP)[0]