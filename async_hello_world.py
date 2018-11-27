import time
import asyncio

start = time.time()


def tic():
    """Retorna time decorrido desde o incio."""
    return 'at %1.1f segundos' % (time.time() - start)


@asyncio.coroutine
def gr1():
    """Método inicial."""
    # Demora a ser executada, mas não queremos esperar
    print('gr1 iniciou a execução: {}'.format(tic()))
    print('gr1 parou momentaneamente...')
    yield from asyncio.sleep(3)
    print('gr1 voltou...')
    print('gr1 terminou a execução: {}'.format(tic()))


@asyncio.coroutine
def gr2():
    """Método secundario."""
    time.sleep(1)
    # Demora a ser executada, mas não queremos esperar
    print('gr2 iniciou a execução: {}'.format(tic()))
    print('gr2 parou momentaneamente...')
    yield from asyncio.sleep(6)
    print('gr2 voltou...')
    print('gr2 terminou a execução: {}'.format(tic()))


@asyncio.coroutine
def gr3():
    """Método final."""
    time.sleep(1)
    print('gr3 executando enquanto as outras estão paradas: {}'.format(tic()))
    print('gr3 parou momentaneamente...')
    yield from asyncio.sleep(9)
    print('gr3 voltou...')
    print('Pronto! todas zeraram: {}'.format(tic()))


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()
