%rebase("base.tpl", title="glavni_meni")

<h1>Glavni meni</h1>

<h4>Pozdravljeni na glavnem meniju! Izberite željeno dejanje</h4>
<p>
    <ul>
        <li>
            Pregled stanja računa
            <form action="/pregled/" method="get">
                <button type="submit">></button>
            </form>
        </li>

        <li>
            Pokaži graf zadnjih transakcij
            <form action="/graf/" method="get">
                <button type="submit">></button>
            </form>
        </li>

        <li>
            Dodaj novo transakcijo
            <form action="/uredi/" method="post">
                <button type="submit">></button>
            </form>
        </li>
    </ul>
</p>