from lib.xmlrpc import SCGIServerProxy
import fields
import math


def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop


class Torrent(dict):
   
    def __init__(self, d, rTorrent):
        dict.__init__(self, d)

        try:
            self["progress"] = round(
                (float(self["bytes_complete"]) / self["size_bytes"]) * 100, 0)
            self["size"] = self["size_bytes"]
        except KeyError:
            print self
        self.rTorrent = rTorrent

    def _filter(self, matches, items):
        def f(item):
            for key, query in matches.iteritems():
                val = item[key]

                if type(query) == "dict":
                    results = []
                    if query.get("gt"):
                        results.append(val > query.get("gt"))
                    if query.get("gte"):
                        results.append(val >= query.get("gt"))
                    if query.get("lt"):
                        results.append(val < query.get("gt"))
                    if query.get("lte"):
                        results.append(val <= query.get("gt"))
                    if query.get("eq"):
                        results.append(val == query.get("gt"))
                    if not all(results):
                        return False
                else:
                    if not query == val:
                        return False
            return True
        return filter(f, items)

    @lazyprop
    def peers(self, **kwargs):
        args = [self["hash"], 0]
        args += [f["name"] + "=" for f in fields.mapping["peers"].values()]
        results = self._parse_multicall_peers(
            fields.mapping["peers"].items(), self.rTorrent.p.multicall(*args))
        if kwargs:
            return self._filter(kwargs, results)

    @lazyprop
    def trackers(self, **kwargs):
        args = [self["hash"], 0]
        args += [f["name"] + "=" for f in fields.mapping["trackers"].values()]
        results = self._parse_multicall_trackers(
            fields.mapping["trackers"].items(), self.rTorrent.t.multicall(*args))
        if kwargs:
            return self._filter(kwargs, results)
        else:
            return results

    @lazyprop
    def files(self, **kwargs):
        args = [self["hash"], 0]
        args += [f["name"] + "=" for f in fields.mapping["files"].values()]
        results = self._parse_multicall_files(
            fields.mapping["files"].items(), self.rTorrent.f.multicall(*args))
        if kwargs:
            return self._filter(kwargs, results)
        else:
            return results

    def _parse_multicall_torrents(self, keys, response):
        return [Torrent([(keys[i][0], keys[i][1]["type"](col)) for i, col in enumerate(row)], self) for row in response]

    def _parse_multicall_peers(self, keys, response):
        return [Peer([(keys[i][0], keys[i][1]["type"](col)) for i, col in enumerate(row)]) for row in response]

    def _parse_multicall_trackers(self, keys, response):
        return [Tracker([(keys[i][0], keys[i][1]["type"](col)) for i, col in enumerate(row)]) for row in response]

    def _parse_multicall_files(self, keys, response):
        return [File([(keys[i][0], keys[i][1]["type"](col)) for i, col in enumerate(row)]) for row in response]

    


class File(dict):
    pass


class Tracker(dict):
    pass


class Peer(dict):
    pass


class rTorrent(SCGIServerProxy):

    def __init__(self, uri):
        SCGIServerProxy.__init__(self, uri)
        self.mapping = fields.mapping["torrents"]

    def _tr_fields(self, attrs):
        return map(lambda x: self.mapping[x]["name"], attrs)

    def torrents(self, view="main", **kwargs):
        args = [view] + [i + "=" for i in self._tr_fields(self.mapping.keys())]
        results = self._parse_multicall(
            self.mapping.items(), self.d.multicall(*args))
        if kwargs:
            return self._filter(kwargs, results)
        else:
            return results

    def _parse_multicall(self, keys, response):
        return [Torrent([(keys[i][0], keys[i][1]["type"](col)) for i, col in enumerate(row)], self) for row in response]

    def torrent(self, info_hash):
        keys = sorted(self.mapping.items(), key=lambda x: x[0])
        response = self.system.multicall([{"methodName": key, "params": [
                                         info_hash]} for key in self._tr_fields(sorted(self.mapping.keys()))])
        return Torrent([(keys[i][0], keys[i][1]["type"](col[0])) for i, col in enumerate(response)], self)

    def _filter(self, matches, items):
        def f(item):
            for key, query in matches.iteritems():
                val = item[key]
                if type(query) == "dict":
                    results = []
                    if query.get("gt"):
                        results.append(val > query.get("gt"))
                    if query.get("gte"):
                        results.append(val >= query.get("gt"))
                    if query.get("lt"):
                        results.append(val < query.get("gt"))
                    if query.get("lte"):
                        results.append(val <= query.get("gt"))
                    if query.get("eq"):
                        results.append(val == query.get("gt"))
                    if not all(results):
                        return False
                else:
                    if not query == val:
                        return False
            return True
        return filter(f, items)
