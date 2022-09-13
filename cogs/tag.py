
import discord,os
from discord.ext import commands

class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot
  
  @commands.hybrid_command(name="pong")
  async def ping_command(self, ctx: commands.Context) -> None:
    """
    This command is actually used as an app command AND a message command.
    This means it is invoked with `?ping` and `/ping` (once synced, of course).
    """

    await ctx.send("Hello!")
    # we use ctx.send and this will handle both the message command and app command of sending.
    # added note: you can check if this command is invoked as an app command by checking the `ctx.interaction` attribute.
    
   
  @commands.hybrid_group(name="tag")
  async def tag(self, ctx: commands.Context) -> None:
    """
    We even have the use of parents. This will work as usual for ext.commands but will be un-invokable for app commands.
    This is a discord limitation as groups are un-invokable.
    """
    ...   # nothing we want to do in here, I guess!
    
  @tag.command(name="logic")
  async def logic(self, ctx: commands.Context) -> None:
    """
    Giới thiệu về logic cơ bản.
    """
    file = discord.File(os.path.join("D:\downloand\laptrinh\Four Gaming\cogs\\filemess\\basic_logic.jpg"))
    await ctx.send('''
- Logic được ví như một bộ xử lý máy tính. bởi vì nó có một công dụng là xử lý lệnh mà các bạn đã nhập vào!

* Vậy chúng ta sử dụng nó như thế nào?
- Nếu các bạn đã từng học qua ``pascal`` thì nó tương tự như vậy!, Nó chỉ phức tạp hơn một tí.
- Thật may mắn ``Anuken`` của chúng ta đã hiểu được chúng ta!! Thay vì gõ code thì chúng ta chỉ đơn giản là kéo và thả lệnh.
- Thêm một vài thao tác nữa thì nó sẵn sàng hoạt động.

* Phương thức hoạt động của Logic.
1. Logic được vận hành theo quy tắc xử lý lệnh từ trên xuông dưới.
2. Sau khi chạy xuống dưới cùng thì sẽ chạm phải hàm ``END`` thì trình xữ lý lệnh sẽ quay lại lên trên cùng và lặp lại quá trình.

Tóm gọn: logic là cách bạn tư duy, bạn tư duy nó dễ thì dễ nó khó thì khó.
Yêu cầu: Bạn phải ít nhất nắm được cách lập trình và chạy lệnh ở pascal lớp 7-9!!! 
      
note: ``JACK.VN`` ''',delete_after=55)
    await ctx.send(file=file,delete_after=55)
  @tag.command(name="set")
  async def set(self, ctx: commands.Context) -> None:
    """
    Giới thiệu về lệnh set.
    """
    file = discord.File(os.path.join("D:\downloand\laptrinh\Four Gaming\cogs\\filemess\\set.png"))
    file2 = discord.File(os.path.join("D:\downloand\laptrinh\Four Gaming\cogs\\filemess\\setvd.png"))
    file3 = discord.File(os.path.join("D:\downloand\laptrinh\Four Gaming\cogs\\filemess\\setvd1.png"))
    await ctx.send('''
- set là một lệnh gán giá trị cho tên biến.
* Cú pháp:
  ```set <tên biến> = <giá trị gán>```
* Cách sử dụng:
- Theo ta thấy lệnh set có hai ô.
  + ô thứ nhất bên trái là ô đặt tên biến mà các bạn muốn nó gán giá trị vào.
    VD: helo, jack ,...
  + ô thứ hai bên phải chính là ô chứa giá trị sẽ gán cho tên biến (có thể là tên hoặc số).
    VD: 124,hehe,@unit,...
  VD: set haha = 99 --> có nghĩa là gán giá trị ``99`` cho ``hah``

* Ứng dụng
- sử dụng lệnh ``set`` để gán tên biến thành một giá trị cố định. 
      
note: ``JACK.VN`` ''',file=file,delete_after=55)
    await ctx.send(file=file2,delete_after=55)
    await ctx.send(file=file3,delete_after=55)
  @tag.command(name="operation",aliases=["op","opera"])
  async def logic(self, ctx: commands.Context) -> None:
    """
    Giới thiệu về lệnh operation.
    """
    file = discord.File(os.path.join("D:\downloand\laptrinh\Four Gaming\cogs\\filemess\\basic_logic.jpg"))
    await ctx.send('''
- ``Operation`` là lệnh tính toán đơn giản.
* Cú pháp:
  ```<tên biến> = <giá trị một> <phép tính> <giá trị hai>```
* Cách sử dụng:
- Theo ta thấy lệnh operation có bốn ô.
  + ô thứ nhất bên trái là ô đặt tên biến mà các bạn muốn, nó gán kết quả tính toán cho tên biến này.
    VD: helo, jack ,...
  + ô giá trị một và hai dùng để chứa các giá trị (có thể là tên hoặc số).
    VD: 124,hehe,@unit,...
  + ô phép tính chứa hầu hết các phép tính có trong lập trình (+ , - , * , / ,...)
      _Trong đó có các phép tính nâng cao như:
        ``ceil``: làm tròn số lên (0.5-->1)
        ``floor``: làm tròn số xuống (0.5-->0)
        ``sqrt``: căn bậc hai
        ``rand <n>``: ngẫu nhiên số từ 0->n
  VD: ``set abc = 99 + 1 --> abc = 100``

* Ứng dụng
- sử dụng lệnh ``operation`` để tính toán các công thức từ đơn giản đến phức tạp ;]]]. 
      
note: ``JACK.VN`` ''',delete_after=55)
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(MyCog(bot))
      

