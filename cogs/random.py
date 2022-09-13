from datetime import datetime
import discord,asyncio
from discord.ext import commands

class ran(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def chat(self,ctx):
        await ctx.send('''
```A. Hướng dẫn mở server mindustry```
- Trên youtube *FOUR GAMING STUDIO* đã làm video hướng dẫn về nó! 
- https://www.youtube.com/channel/UCJrRWlDXB0C9AC_ti84gUrA
```Hướng dẫn mở server mindustry trên máy tính```
- Đầu tiên các bạn lên (https://anuke.itch.io/mindustry/download/eyJpZCI6MTQwMTY5LCJleHBpcmVzIjoxNjYyNjQ3OTMxfQ%3d%3d.7c3VNJRePMtodkZZl2SQLg51g7g%3d) 
và tải cho mình flie: `[Server]Mindustry.zip` (phiên bản tùy các bạn) --->> sau đó giải nén nó ra. 
- Sau đó các bạn sẽ thấy trong tệp vừa giải nén thì có một file: `server.jar`. 
- Để chạy được file: `server.jar` này các bạn hãy lên (https://www.java.com/en/) tải xuống `java` và cài đặt nó (cách cài đặt trên youtube).
- Sau khi cài đặt `java` xong thì bây gờ có thể chạy file: `server.jar` lúc nãy.
- Nhấn đúp chuột vào file: `sever.jar` nó sẽ tạo một tệp `config` đây là nơi chúng ta thêm `maps` và `mods`.
- Bây giờ các bạn hãy chạy một trong hai file: `run_server.bat` hoặc `run_server.sh`, tùy hệ điều hành nó sẽ chạy và hiển thị lên một `cmd`.
''')
        await ctx.send('''
- Các bạn nhập `host` trong `cmd` thì nó sẽ mở máy chủ cục bộ. (vào game check đi :)))
- `Máy chủ cục bộ`: những người dùng chung mạng mới chơi được với nhau như `zero tire one`.
- `Máy chủ cộng đồng`: ở đâu cũng chơi đc :}}
- Để mở được `máy chủ cục bộ` thì các bạn phải mở `quy tắc chuyển tiếp` (port forwarding) trên cục `modem wifi`. 
- Cách mở cổng thì mình không thể hướng dẫn chi tiết vì mỗi `modem wifi` có một cách mở khác nhau.
- Cách đơn giản nhất là: các bạn thấy số điện thoại trên `modem wifi chứ` gọi vào số đó đi :}}
''')
        await ctx.send('''
```B. Cách mở quy tắc chuyển tiếp (port forwarding) cơ bản:```
B1. Xác định IP + tên máy
     + Vào `cmd` của máy tính và nhập `ipconfig`.
     + Tìm dòng `IPv4 Address` và nhớ `ip` này
     + Chuột phải vào `start` (Windown) vào `sytem` để tấy lên máy tính của các bạn.
B2. Các bạn tới cục `modem wifi` của mình và tìm:
     + `Tên đăng nhập` + `mật khẩu`.
     + `Địa chỉ cục modem wifi` (168.179.1.n) + `Tên modem wifi`.
B3. Lên google nhập địa chỉ cục `modem wifi` vào thanh tìm kiếm.
     + `Đăng nhập` với tên đăng nhập và mật khẩu các bạn đã tìm.
     + Đăng nhập đúng thì tên modem trên góc trái của trang web sẽ trùng với tên `modem wifi` của các bạn.
B4. Tùy vào modem wifi các bạn hãy tìm tới thanh Quy tắc chuyển tiếp (Forward Rules)
     * Nhấp vào thanh `Cấu hình ánh xạ cổng` (Port Mapping Configuration)
      + Trong này các bạn hãy nhấp nút `mới` hoặc `thêm` (add, new).
    +  Tiếp đó các bạn cài đặt như này:

        `Type`:                [v] User-defined           [] Application

        `Application`:        [giữ nguyên]

        `Enable Port Mapping`:    [v]

        `Mapping Name`:         [đặt tên cho cái cổng này]

        `WAN Name`:             [giữ nguyên]

        `Internal Host`:         [IPv4 lúc nãy]--[tên máy các bạn]

        `External Source IP Address`:    [để trống]--[để trống]

     + nhấp vào `thêm, mới` (add, new) phía dưới `bên phải` trang web.

        `Protocol`:              [TCP/UDP]

        `Internal port number`:    [6567]--[6567]

        `External port number`:    [6567]--[6567]

        `External source port number`:    [để trống]--[để trống]

    * Nhấp vào `cài đặt, ứng dụng` (apply) để cài đặt `đợi 5s` để đợi nó cài đặt cổng. 
''')
        await ctx.send('''
- Bây giờ các bạn hãy vào thư mục chứa file: `server.jar` và chạy file: `run_server.bat` hoặc `run_server.sh` để chạy `server`.
  + nhập lệnh host để mở máy chủ.
- Vào game nếu thấy trong cục bộ đã lên server thì các bạn hãy lên (https://canyouseeme.org/) và `sao chép ip` của máy các bạn.
- Vào lại game nhấp vào `thêm máy chủ` và `dán ip lúc` nãy và nhấp thêm.
  + Nếu thấy `server` thì chúc mùng các bạn đã `host máy chủ thành công`!!!
  + Nếu không thấy thì các bạn hãy kiểm tra `quy tắc chuyển tiếp` (Forward Rules) đã đúng hay chưa hoặc nếu là `laptop` thì các bạn hãy cài đặt `ip tĩnh` cho máy tính các bạn nhé.
  + Nếu set `ip tĩnh` xong vẫn chưa thấy `server` thì các bạn hãy tới `C`!!
''')
        await ctx.send('''
```C. Hưỡng dân mở tường lửa(Windows defender firewall)```
**I. Giới thiệu**
- `Tường lửa` là một ứng dụng có sắn của `windows` giúp ngăn chặn những rủi ro từ `không gian mạng`!!
- Chính `tường lửa` này đã chặn `cổng 6567 server` chúng ta vậy nên chúng ta `cần cấp phép cổng 6567 đi qua`.
**II. Cách mở cổng**
B1. Các bạn hãy vào `công cụ tìm kiếm windows` và tìm kiếm với từ khóa `Windows defender firewall` và vào ứng dụng.
B2. Trong ứng dụng các bạn hãy nhấp vào `Advanced settings`.
B3. Trong hộp thoại `Windows defender firewall with Advanced security`:
    + Cách bạn hãy nhấp vào `Inbound Rules`, tiếp đó nhấp vào new Rule:
        & Tạo cho mình hai cổng `6567` cho `tcp` và `udp`.
        & Đảm bảo hai cổng này được `bật`.
        & Hướng dẫn chi tiết trên kênh `FOUR GAMING STUDIO`.
    + Cách bạn hãy nhấp vào `Outbound Rules`, tiếp đó nhấp vào `new Rule`:
        & Tạo cho mình hai cổng `6567` cho `tcp` và `udp`.
        & Đảm bảo hai cổng này được `bật`.
        & Hướng dẫn chi tiết trên kênh `FOUR GAMING STUDIO`

**Xong rồi server các bạn đã sắn sàng để online!!!!!!**
''')
async def setup(bot):
    await bot.add_cog(ran(bot))


